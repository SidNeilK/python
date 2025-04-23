class Television:
    """
    This class models a basic TV with simple controls for power, volume, channels, and muting.
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3
    previous_volume: int = 0

    def __init__(self) -> None:
        """
        Sets up the TV with default settings: off, unmuted, volume at 0, and channel at 0.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Flips the TV's power switch on or off.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Toggles mute on or off. When muting, saves the current volume and drops it to 0.
        When unmuting, restores the saved volume.
        Only works if the TV is powered on.
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
        Bumps the channel up by one, if it goes past the max channel, it loops back to the minimum.
        Only works if the TV is on.
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Lowers the channel by one, if it goes below the minimum, it loops to the max channel.
        Only works if the TV is on.
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Turns the volume up by one, unmutes the TV if muted, won't go above max volume.
        Only works if the TV is on.
        """
        if self.__status:
            if self.__muted:
                self.mute()
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Turns the volume down by one, unmutes the TV if muted, won't go below minimum volume.
        Only works if the TV is on.
        """
        if self.__status:
            if self.__muted:
                self.mute()
            self.__volume -= 1
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Shows the TV's current state, including power, channel, and volume.
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
