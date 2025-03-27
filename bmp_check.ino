#include "Wire.h"
#include "SFE_BMP180.h"

SFE_BMP180 pressure; // создаем объект pressure
#define ALTITUDE 1655.0 // высота офиса SparkFun, штат Колорадо, в метрах

void setup(){
   Serial.begin(9600); 
   pressure.begin();   
}

void loop(){
   char status;
   double T,P,p0,a;

   // для точного измерения, следует знать высоту, на которой производятся замеры
   // в этом примере используется константа ALTITUDE
   Serial.println();
   Serial.print("provided altitude: ");
   Serial.print(ALTITUDE,0);
   Serial.println(" meters");
  
   // перед измерением давления, следует узнать температуру
   // если запрос успешен, то возвращается время ожидания в миллисекундах
   // если запрос на измерение температуры не успешен, то возвращается 0
   status = pressure.startTemperature();
   if (status != 0){
      delay(status);

      // результат измерения температуры сохраняется в переменной T
      status = pressure.getTemperature(T);
      if (status != 0){
         Serial.print("temperature: ");
         Serial.print(T,2);
         Serial.println(" deg C");

         // запускаем измерение давления
         // если запрос успешен, возвращается время ожидания в миллисекундах
         // если запрос на измерение давления не успешен, возвращается 0
         status = pressure.startPressure(3);
         if (status != 0){
            delay(status);

            status = pressure.getPressure(P,T);
            if (status != 0){
               Serial.print("absolute pressure: ");
               Serial.print(P,2);
               Serial.print(" mb, ");
               Serial.print(P*0.0295333727,2);
               Serial.println(" inHg");

              // датчик bmp180 возвращает абсолютное давление, которое зависит от высоты
              // параметры: P = абсолютное давление в мб, ALTITUDE = текущая высота в м.
              // результат: p0 = давление с компенсацией на уровне моря в мбар
              p0 = pressure.sealevel(P,ALTITUDE);
              Serial.print("relative (sea-level) pressure: ");
              Serial.print(p0,2);
              Serial.print(" mb, ");
              Serial.print(p0*0.0295333727,2);
              Serial.println(" inHg");
           }
        else Serial.println("error retrieving pressure measurement\n");
      }
      else Serial.println("error starting pressure measurement\n");
    }
    else Serial.println("error retrieving temperature measurement\n");
  }
  else Serial.println("error starting temperature measurement\n");

  delay(5000);
}
