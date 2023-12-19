import random

class NumericLottery:
    def __init__(self, title):
        self._title = title
    
    def introduction(self):
        print("*" * len(self._title), self._title, "*" * len(self._title), sep="\n", end="\n")

    def determine_column_count(self):
        while True:
            try:
                column_count = int(input('How many columns would you like to generate?  : '))
                break  
            except ValueError:
                print('An integer was not entered. Please try again... ')

        return column_count

    def generate_lottery_columns(self):
        count = self.determine_column_count()
        columns = []
        counter = 0

        while counter < count:
            column = random.sample(range(1, 51), 6)  
            column.sort()

            if column not in columns:
                columns.append(column)
                counter += 1
                print("{}. column = {}".format(counter, column))

if __name__ == "__main__":
    title = "Hello Numeric Lottery"
    nl = NumericLottery(title)
    nl.introduction()
    nl.generate_lottery_columns()
