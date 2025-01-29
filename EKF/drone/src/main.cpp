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
#include <ekf.hpp>
#include "MPU9250.h"

template <typename T>
internal::tmp<Vector<T>> && f(const Vector<T> &x, const Vector<T> &u, const Vector<T> &c)
{
    auto *ret = internal::tmp<Vector<T>>::get(x.size()); // ask for a temporary variable of the same size as x
    (*ret)[0] = x[0] + c[0] *(u[0]/c[1] - (x[0]-c[3])/c[2]); // compute the new temperature
    return internal::move(*ret); // return the temporary variable
}

// simple measurement function
template <typename T>
internal::tmp<Vector<T>> && h(const Vector<T> &x, const Vector<T> &c)
{
    auto *ret = internal::tmp<Vector<T>>::get(1); // ask for a temporary variable of size 2
    (*ret)[0] = x[0];
    return internal::move(*ret);
}



MPU9250 IMU(Wire,0x68);


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