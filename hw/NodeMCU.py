import machine

from hw.Board import Board


class NodeMCU(Board):

    pins = {

        "BTN_FLASH" :   machine.Pin(0, machine.Pin.IN),
        "BTN_USER"  :   machine.Pin(16, machine.Pin.IN),
        "LED_BLUE"  :   machine.Pin(2, machine.Pin.OUT),

    }

    def __init__(self):
        Board.__init__(self, self.pins)


    def get_pin_mapping(self):
        return Board.get_pin_mapping(self)


    def set_pin_mapping(self, pin_mapping):
        Board.set_pin_mapping(self, pin_mapping)


    def get_pin(self, pin_key):
        return Board.get_pin_mapping(self)[pin_key]


    def set_pin(self, pin_key, pin_value):
        Board.set_pin(self, pin_key, pin_value)


    def get_pin_value(self, pin):
        return Board.get_pin_value(self, pin)

    def blink_blue_led(self, times, delay):
        Board.blink_onboard_led(self, times, delay, self.get_pin("LED_BLUE"))

    def get_flash_button_events(self, on_single_click, on_double_click):
        from machine import Timer

        Board.button_click_counter['flash'] = 0

        pin = self.get_pin("BTN_FLASH")

        tim = Timer(0)
        tim.init(period=200, mode=Timer.PERIODIC, callback=lambda t: Board.get_onboard_button_events(self, pin, 'flash', on_single_click, on_double_click))


    def get_user_button_events(self, on_single_click, on_double_click):
        from machine import Timer

        Board.button_click_counter['user'] = 0

        pin = self.get_pin("BTN_USER")

        tim = Timer(0)
        tim.init(period=200, mode=Timer.PERIODIC, callback=lambda t: Board.get_onboard_button_events(self, pin, 'user', on_single_click, on_double_click))


    def scan_wifi(self):
        import network
        return Board.scan_wifi(self, network.STA_IF)

    def connect_to_wifi(self, ssid, password, wait_for_ip):
        import network
        return Board.connect_to_wifi(self, ssid, password, network.STA_IF, wait_for_ip)