#include "MyLittleFactory.h"

void setup() {
    setup_serial();
    setup_components();
    build_command_list();
}
void loop() {
    unsigned char cmd[16];
    if(read_command(cmd)){
      execute_command(cmd);
    };
    delay(10);  //This delay is necessary due to serial timing constraints
}
