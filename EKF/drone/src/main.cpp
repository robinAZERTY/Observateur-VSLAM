/*
____________STATE ESTIMATE VECTOR______________

        State                   unit        index       length
orientation(quaternion)                     0:4         4
position(xyz)                   m           4:7         3
velocity(xyz)                   m/s         7:10         3
gyr_bias_correction(xyz)        rad/s       10:13        3
acc_bias_correction(xyz)        m/s²        13:16       3
gyr_ortho_correction(3*3)                   16:25       9
acc_ortho_correction(3*3)                   25:34       9

___________COMMANDS VECTOR_____________________

        State                   unit        index       length
gyroscopes(xyz)                 rad/s       0:3         3       
accelerometers(xyz)             m/s²        3:6         3


___________SENSOR VECTORS_____________________

        State                   unit        index       length
position(xyz)                   m           0:3         3


delay for prediction: 6ms
delay for correction: 1ms

*/

#include <Arduino.h>


// put function declarations here:
int myFunction(int, int);

void setup() {
  // put your setup code here, to run once:
  int result = myFunction(2, 3);
}

void loop() {
  // put your main code here, to run repeatedly:
}

// put function definitions here:
int myFunction(int x, int y) {
  return x + y;
}