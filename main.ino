#include <SPI.h>
#include <SD.h>
#include <Wire.h>
#include <MPU6050.h>
#include <SFE_BMP180.h>
#include <TinyGPS++.h>
#include <SoftwareSerial.h>
#include <LoRa.h>

MPU6050 mpu;
SFE_BMP180 pressure;
TinyGPSPlus gps;
SoftwareSerial ss(4, 3); // RX, TX

File myFile;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();
  pressure.begin();
  ss.begin(9600);
  LoRa.begin(433E6);

  if (!SD.begin(10)) {
    Serial.println("Ошибка инициализации SD карты!");
    return;
  }
  Serial.println("SD карта инициализирована.");

  if (!mpu.testConnection()) {
    Serial.println("MPU6050 не подключен!");
    while (1);
  }

  if (!LoRa.begin(433E6)) {
    Serial.println("Ошибка инициализации LoRa!");
    while (1);
  }
}

void loop() {
  int mq135Value = analogRead(A0);
  int mq9Value = analogRead(A1);
  int mq131Value = analogRead(A2);
  int lm35Value = analogRead(A3);
  int voltmeterValue = analogRead(A6);

  int16_t ax, ay, az;
  mpu.getAcceleration(&ax, &ay, &az);

  char status;
  double T, P;
  status = pressure.startTemperature();
  if (status != 0) {
    delay(status);
    status = pressure.getTemperature(T);
    if (status != 0) {
      status = pressure.startPressure(3);
      if (status != 0) {
        delay(status);
        status = pressure.getPressure(P, T);
      }
    }
  }

  while (ss.available() > 0) {
    gps.encode(ss.read());
  }

  float latitude = gps.location.lat();
  float longitude = gps.location.lng();

  float lightLevel = readLightLevel();

  myFile = SD.open("data.txt", FILE_WRITE);
  if (myFile) {
    myFile.print("MQ-135: "); myFile.println(mq135Value);
    myFile.print("MQ-9: "); myFile.println(mq9Value);
    myFile.print("MQ-131: "); myFile.println(mq131Value);
    myFile.print("LM35: "); myFile.println(lm35Value);
    myFile.print("Voltmeter: "); myFile.println(voltmeterValue);
    myFile.print("Accel: "); myFile.print(ax); myFile.print(", "); myFile.print(ay); myFile.print(", "); myFile.println(az);
    myFile.print("Temperature: "); myFile.println(T);
    myFile.print("Pressure: "); myFile.println(P);
    myFile.print("Latitude: "); myFile.println(latitude);
    myFile.print("Longitude: "); myFile.println(longitude);
    myFile.print("Light Level: "); myFile.println(lightLevel);
    myFile.close();
    Serial.println("Данные записаны на SD карту.");
  } else {
    Serial.println("Ошибка открытия файла!");
  }

  LoRa.beginPacket();
  LoRa.print("MQ-135: "); LoRa.println(mq135Value);
  LoRa.print("MQ-9: "); LoRa.println(mq9Value);
  LoRa.print("MQ-131: "); LoRa.println(mq131Value);
  LoRa.print("LM35: "); LoRa.println(lm35Value);
  LoRa.print("Voltmeter: "); LoRa.println(voltmeterValue);
  LoRa.print("Accel: "); LoRa.print(ax); LoRa.print(", "); LoRa.print(ay); LoRa.print(", "); LoRa.println(az);
  LoRa.print("Temperature: "); LoRa.println(T);
  LoRa.print("Pressure: "); LoRa.println(P);
  LoRa.print("Latitude: "); LoRa.println(latitude);
  LoRa.print("Longitude: "); LoRa.println(longitude);
  LoRa.print("Light Level: "); LoRa.println(lightLevel);
  LoRa.endPacket();

  delay(1000);
}

float readLightLevel() {
  Wire.beginTransmission(0x23);
  Wire.write(0x10);
  Wire.endTransmission();
  delay(200);

  Wire.requestFrom(0x23, 2);
  uint16_t level = Wire.read();
  level <<= 8;
  level |= Wire.read();
  return level / 1.2;
}
