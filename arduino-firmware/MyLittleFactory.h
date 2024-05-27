
/**
Library for MK2Robot control and some effectors we use in The Little Factory
see project repo @ https://github.com/Beauchef-Proyecta/mlf

This library has been written following the Arduino documentation and guidelines
https://www.arduino.cc/en/Hacking/LibraryTutorial
https://www.arduino.cc/en/Reference/APIStyleGuide
*/


/** GPIO PINOUT */
#define SERVO_J0        3
#define SERVO_J1        5
#define SERVO_J2        6
#define SERVO_J3        9   // gripper rotor, new dof

#define GRIPPER_SERVO   10  // manage grappling
#define EXTRA_SERVO     11  // extra servo
#define RELAY_1         7   // manage first relay
#define RELAY_2         8   // manage second relay

#define CELL_CLK        A0  
#define CELL_DOUT       A1


#define TRIGGER_PIN     12  // manage proximity sensor
#define ECHO_PIN        13  // manage proximity sensor

#define BELT_STATUS     8   // manage belt status
#define BELT_DIRECTION  4   // manage belt forward-backward

/** HOME VALUES */
#define HOME_J0         90
#define HOME_J1         90
#define HOME_J2         90
#define HOME_J3         90
#define HOME_RELAY_1    1
#define HOME_RELAY_2    1
#define HOME_GRIPPER    120
#define HOME_EXTRA      0


/** SERIAL CONSTANTS */
#define HEADER          0xA0

/** COMMAND LIST ADDRESSES */
#define CMD_JOINT       0x10
#define CMD_BELT        0x20
#define CMD_GRIPPER     0x30
#define CMD_MAGNET      0x40
#define CMD_RELAY_1     0x50
#define CMD_RELAY_2     0x60
#define CMD_EXTRA       0x70
#define CMD_PROXIMITY   0xA0
#define CMD_LASER       0xB0
#define CMD_WEIGHT      0x80
#define CMD_DISTANCE    0x90

typedef int (*func_ptr_t)(char*);


/** MAIN FUNCTIONS */

void build_command_list();

void setup_serial();

void setup_components();

bool read_command(unsigned char* buffer);

int execute_command(unsigned char* cmd);
