
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
#define GRIPPER_RELAY   7   // manage relay
#define BELT_STATUS     8     // manage belt status
#define BELT_DIRECTION  4  // manage belt forward-backward

/** HOME VALUES */
#define HOME_J0         90
#define HOME_J1         90
#define HOME_J2         90
#define HOME_J3         90
#define HOME_RELAY      1
#define HOME_GRIPPER    180


/** SERIAL CONSTANTS */
#define HEADER          0xA0

/** COMMAND LIST ADDRESSES */
#define CMD_JOINT       0x10
#define CMD_BELT        0x20
#define CMD_GRIPPER     0x30
#define CMD_MAGNET      0x40
#define CMD_PROXIMITY   0xA0
#define CMD_LASER       0xB0

typedef int (*func_ptr_t)(char*);


/** MAIN FUNCTIONS */

void build_command_list();

void setup_serial();

void setup_components();

bool read_command(char* buffer);

int execute_command(char* cmd);
