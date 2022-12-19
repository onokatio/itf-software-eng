class TelephoneNumber:
    _area_code: str  # 勤務先の市外局番
    _number: str  # 勤務先の市内電話番号

    @property
    def number(self):
        return self._number

    @property
    def area_code(self):
        return self._area_code

    @number.setter
    def number(self, val):
        self._number = val

    @area_code.setter
    def area_code(self, val):
        self._area_code = val

    def telephone_number(self):
	    return self._area_code + "-" + self._number
