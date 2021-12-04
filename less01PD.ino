int data;
void setup() { 
  Serial.begin(9600); //инициализируем последовательную связь на COM порту со скоростью 9600 бод/с
  pinMode(LED_BUILTIN, OUTPUT); //задаем режим работы на вывод данных для контакта 13, к которому подключен светодиод
  digitalWrite (LED_BUILTIN, LOW);
  Serial.println("Hi!, I am Arduino");
}
 
void loop() {
while (Serial.available()){
  data = Serial.read();
}
  if (data == '1'){
    digitalWrite (LED_BUILTIN, HIGH);
  }
  else if (data == '0'){
    digitalWrite (LED_BUILTIN, LOW);
  }
}
