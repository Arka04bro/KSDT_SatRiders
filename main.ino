#include <SPI.h>
#include <SD.h>
#include <Wire.h>
#include <Adafruit_BMP085.h>
#include <Adafruit_MPU6050.h>
#include <TinyGPS++.h>
#include <SoftwareSerial.h>

#define SD_CS_PIN 4
#define LOG_INTERVAL 5000
#define TCA9548A_ADDR 0x70
#define GPS_BAUDRATE 9600

enum I2C_CHANNELS {
  CHANNEL_MPU9150 = 0,
  CHANNEL_BMP180 = 1
};

struct SensorData {
  unsigned long timestamp;
  float temperature;
  float pressure;
  float altitude;
  double latitude;
  double longitude;
  int mq135;
  int mq137;
  int mq131;
  float accelX;
  float accelY;
  float accelZ;
};

Adafruit_BMP085 bmp180;
Adafruit_MPU6050 mpu9150;
TinyGPSPlus gpsParser;
SoftwareSerial gpsSerial(3, 2);
File dataFile;
SensorData currentData;

void SelectI2CChannel(uint8_t channel) {
  Wire.beginTransmission(TCA9548A_ADDR);
  Wire.write(1 << channel);
  Wire.endTransmission();
}

bool InitializeSDCard() {
  if (!SD.begin(SD_CS_PIN)) return false;
  if (!SD.exists("log.csv")) {
    dataFile = SD.open("log.csv", FILE_WRITE);
    dataFile.println("Timestamp,Temp(C),Pressure(hPa),Alt(m),Lat,Lon,MQ135,MQ137,MQ131,AccX,AccY,AccZ");
    dataFile.close();
  }
  return true;
}

void ReadEnvironmentalSensors() {
  SelectI2CChannel(CHANNEL_BMP180);
  currentData.temperature = bmp180.readTemperature();
  currentData.pressure = bmp180.readPressure() / 100.0;
  currentData.altitude = bmp180.readAltitude();
}

void ReadMotionSensors() {
  SelectI2CChannel(CHANNEL_MPU9150);
  sensors_event_t accel, gyro, temp;
  mpu9150.getEvent(&accel, &gyro, &temp);
  currentData.accelX = accel.acceleration.x;
  currentData.accelY = accel.acceleration.y;
  currentData.accelZ = accel.acceleration.z;
}

void ReadGasSensors() {
  currentData.mq135 = analogRead(A0);
  currentData.mq137 = analogRead(A1);
  currentData.mq131 = analogRead(A2);
}

void ReadGPSData() {
  while (gpsSerial.available() > 0) {
    if (gpsParser.encode(gpsSerial.read())) {
      if (gpsParser.location.isValid()) {
        currentData.latitude = gpsParser.location.lat();
        currentData.longitude = gpsParser.location.lng();
      }
    }
  }
}

void LogSensorData() {
  dataFile = SD.open("log.csv", FILE_WRITE);
  if (dataFile) {
    String dataString = 
      String(currentData.timestamp) + "," +
      String(currentData.temperature, 2) + "," +
      String(currentData.pressure, 2) + "," +
      String(currentData.altitude, 2) + "," +
      String(currentData.latitude, 6) + "," +
      String(currentData.longitude, 6) + "," +
      currentData.mq135 + "," +
      currentData.mq137 + "," +
      currentData.mq131 + "," +
      String(currentData.accelX, 2) + "," +
      String(currentData.accelY, 2) + "," +
      String(currentData.accelZ, 2);
      
    dataFile.println(dataString);
    dataFile.close();
  }
}

void setup() {
  Serial.begin(9600);
  Wire.begin();
  gpsSerial.begin(GPS_BAUDRATE);

  SelectI2CChannel(CHANNEL_BMP180);
  if (!bmp180.begin()) Serial.println("BMP180 Init Failed");
  
  SelectI2CChannel(CHANNEL_MPU9150);
  if (!mpu9150.begin()) Serial.println("MPU9150 Init Failed");
  
  if (!InitializeSDCard()) Serial.println("SD Card Init Failed");
  
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);

  delay(30000);
}

void loop() {
  currentData.timestamp = millis();
  
  ReadEnvironmentalSensors();
  ReadMotionSensors();
  ReadGasSensors();
  ReadGPSData();
  LogSensorData();

  delay(LOG_INTERVAL);
}
