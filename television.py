class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    previous_volume = 0

    def __intit__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
    def power(self):
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        if self.__status:
            if not self.__muted:
                Television.previous_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
                self.__muted = True
            else:
                self.__volume = Television.previous_volume
                self.__muted = False
    def channel_up(self):
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television .MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.mute()
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.mute()
            self.__volume -= 1
            if self.__volume < Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'