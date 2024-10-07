class Tv:
    def __init__(self):
        self._volume = 0
        self._is_on = False
        self._channel = 0
        self.previous_channel = None
        self.previous_volume = None

    def get_tv_state(self):
        return self._is_on

    def turn_on(self):
        self._is_on = True
        if self.previous_channel is not None:
            self._channel = self.previous_channel

    def turn_off(self):
        self._is_on = False
        self.previous_channel = self._channel  # Store the current channel before turning off
        self._volume = 0  # Reset the volume when turned off

    def get_channel(self):
        if self._is_on:
            return self._channel

    def set_channel(self, channel_number):
        if self.is_valid_channel(channel_number) and self._is_on:
            self._channel = channel_number

    def is_valid_channel(self, channel_number):
        return 0 <= channel_number <= 100

    def is_valid_volume(self, volume):
        return 0 <= volume <= 10

    def channel_up(self):
        if self._is_on and self._channel < 100:
            self._channel += 1

    def channel_down(self):
        if self._is_on and self._channel > 0:
            self._channel -= 1

    def get_volume(self):
        return self._volume

    def set_volume(self, volume_number):
        if self.is_valid_volume(volume_number) and self._is_on:
            self._volume = volume_number

    def volume_up(self):
        if self._is_on and self._volume < 10:
            self._volume += 1

    def volume_down(self):
        if self._is_on and self._volume > 0:
            self._volume -= 1

    def mute(self):
        if self._is_on:
            if self._volume != 0:
                self.previous_volume = self._volume
            self._volume = 0

    def unmute(self):
        if self._is_on and self.previous_volume is not None:
            self._volume = self.previous_volume
