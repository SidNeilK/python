class Television:
    """
    A class to simulate a simple television with basic functionality like power,
    volume, channels, and muting
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3
    previous_volume: int = 0

    def __init__(self) -> None:
        """
        Initialize the default settings of power off, not muted,
        volume 0 and channel 0
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
    def power(self) -> None:
        """
        Toggle the power status of the TV
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Toggle the muted status of the TV
        IF unmuted, saves the current volume and sets the volume to the minimum
        IF muted, restores the previous volume
        Only works if the TV is on
        """
        if self.__status:
            if not self.__muted:
                Television.previous_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
                self.__muted = True
            else:
                self.__volume = Television.previous_volume
                self.__muted = False
    def channel_up(self) -> None:
        """
        Increase the channel by one
        IF the channel passes MAX_CHANNEL, wraps around to MIN_CHANNEL
        Only works if the TV is on
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television .MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decrease the channel by one
        IF the channel passes MIN_CHANNEL, wraps around to MAX_CHANNEL
        Only works if the TV is on
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increases the volume by one
        Automatically unmutes the TV
        Caps at MAX_VOLUME
        Only works if the TV is on
        """
        if self.__status:
            if self.__muted:
                self.mute()
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Decreases the volume by one
        Automatically unmutes the TV
        Minimum is MIN_VOLUME
        Only works if the TV is on
        """
        if self.__status:
            if self.__muted:
                self.mute()
            self.__volume -= 1
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Returns the status of the TV including power, channel, and volume
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'