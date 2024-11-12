
const int IN1 = 5;
const int IN2 = 6;
const int IN3 = 9;
const int IN4 = 10;
char ori;
String path[] = {"S", "+y", "+x", "-y", "+x", "-y", "-x", "-y", "-x", "+y", "F"};
int path_length = sizeof(path) / sizeof(path[0]);
if (path[1]=="+y"){
  ori = 'N';
}
else if (path[1]=="+x"){
  ori = 'E';
}
else if (path[1]=="-y"){
  ori = 'S';
}
else{
  ori = 'W';
}

void setup() {
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
void forward(){
  analogWrite(IN1, 0);
  analogWrite(IN2, 120);
  analogWrite(IN3, 0);
  analogWrite(IN4, 120);
}
void turn_left(){
  analogWrite(IN1, 120);
  analogWrite(IN2, 0);
  analogWrite(IN3, 0);
  analogWrite(IN4, 120);
}
void turn_right(){
  analogWrite(IN1,0);
  analogWrite(IN2,120);
  analogWrite(IN3,120);
  analogWrite(IN4,0);
}
void stop(){
  analogWrite(IN1, 0);
  analogWrite(IN2, 0);
  analogWrite(IN3, 0);
  analogWrite(IN4, 0);
}
  
}

void loop() {
  for (int i=0; i<path_length; i++){
    if (path[i]=="S"){
      continue;
    }


    else if (path[i]=="F"){
      stop();
      delay(20000);
    }


    else if (path[i]=="+y"){
      if (ori == 'N'){
        forward();
        delay(3000)
      }
      else if (ori == 'E'){
        turn_left();
        delay(1000);
        forward();
        delay(3000);
        ori = 'N';
      }
      else if (ori == 'W'){
        turn_right();
        delay(1000);
        forward();
        delay(3000);
        ori = 'N';
      }
    }


    else if (path[i]=="+x"){
      if (ori == 'N'){
        turn_right();
        delay(1000);
        forward();
        delay(3000);
        ori = 'E';
      }
      else if (ori == 'E'){
        forward();
        delay(3000);
      }
      else if (ori == 'S'){
        turn_left();
        delay(1000);
        forward();
        delay(3000);
        ori = 'E';
      }
    }


    else if (path[i]=="-y"){
      if (ori == 'S'){
        forward();
        delay(3000)
      }
      else if (ori == 'W'){
        turn_left();
        delay(1000);
        forward();
        delay(3000);
        ori = 'S';
      }
      else if (ori == 'E'){
        turn_right();
        delay(1000);
        forward();
        delay(3000);
        ori = 'S';
      }
    }


    else{
      if (ori == 'W'){
        forward();
        delay(3000)
      }
      else if (ori == 'N'){
        turn_left();
        delay(1000);
        forward();
        delay(3000);
        ori = 'W';
      }
      else if (ori == 'S'){
        turn_right();
        delay(1000);
        forward();
        delay(3000);
        ori = 'W';
      }
    }
  }


}
