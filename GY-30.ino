#include <Wire.h>

// Адрес датчика (0x23 или 0x5C в зависимости от состояния пина ADDR)
#define BH1750_ADDRESS 0x23

// Режимы работы
#define BH1750_CONTINUOUS_HIGH_RES_MODE 0x10

void setup() {
  Serial.begin(9600);
  Wire.begin();
  
  // Инициализация датчика в режиме непрерывных измерений с высоким разрешением
  Wire.beginTransmission(BH1750_ADDRESS);
  Wire.write(BH1750_CONTINUOUS_HIGH_RES_MODE);
  Wire.endTransmission();
  
  delay(300); // Датчику нужно время для инициализации
}

void loop() {
  uint16_t raw_value = readLightIntensity();
  float lux = raw_value / 1.2; // Конвертация в люксы
  
  Serial.print("Освещенность: ");
  Serial.print(lux);
  Serial.println(" лк");
  
  delay(1000);
}

uint16_t readLightIntensity() {
  Wire.requestFrom(BH1750_ADDRESS, 2);
  
  if (Wire.available() == 2) {
    uint16_t value = Wire.read() << 8 | Wire.read();
    return value;
  }
  
  return 0; // Возвращаем 0 при ошибке чтения
}
