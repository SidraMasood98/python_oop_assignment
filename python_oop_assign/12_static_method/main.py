class TemperatureConverter:

    @staticmethod
    def  celcius_to_farenheit(c):
        return (c * 9/5) + 32
    
if __name__ == "__main__":
    print("Farenheit:", TemperatureConverter.celcius_to_farenheit(3))