//https://3drob.ru/stati/pro_arduino/datchiki/3_h_osevoy_giroskop_i_akselerometr_gy_521_mpu_6050#:~:text=3-х%20осевой%20гироскоп%20и,GY-521%20(MPU%206050)
#include "I2Cdev.h"
#include "MPU6050.h"
#define TIME_OUT 20
MPU6050 accgyro;
unsigned long int t1;  
void setup() {
Serial.begin(9600);
accgyro.initialize();
}
void loop() {
long int t = millis();
if( t1 < t ){
int16_t ax, ay, az, gx, gy, gz;
t1 = t + TIME_OUT;
accgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
Serial.println(ax);
}
}
