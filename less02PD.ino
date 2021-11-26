#define P_RED 11
#define P_GREEN 10
#define P_BLUE 9

bool flagR = HIGH;
bool flagG = HIGH;
bool flagB = LOW;

int data;

void color(int pC, bool *flagColor) {
  *flagColor = !(*flagColor);
  digitalWrite (pC, *flagColor);
}

void setup() {
  Serial.begin(9600); //инициализируем последовательную связь на COM порту со скоростью 9600 бод/с
  pinMode(LED_BUILTIN, OUTPUT); //задаем режим работы на вывод данных для контакта 13, к которому подключен светодиод
  digitalWrite (LED_BUILTIN, LOW);
  Serial.println("Hi!, I am Arduino");

  pinMode(P_RED, OUTPUT);
  pinMode(P_GREEN, OUTPUT);
  pinMode(P_BLUE, OUTPUT);
}

void loop() {
  while (Serial.available()) {
    data = Serial.read();
  }
  switch (data) {
    case '1':
      color(P_RED, &flagR);
      data = 0;
      break;
    case '2':
      color(P_GREEN, &flagG);
      data = 0;
      break;
    case '3':
      color(P_BLUE, &flagB);
      data = 0;
      break;
  }
}
