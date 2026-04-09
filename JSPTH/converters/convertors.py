class UnitConvertor:
    """
    A class to convert between different units of measurement.
    """

    conversion_factors = {
        ('meters', 'kilometers'): 0.001,
        ('kilometers', 'meters'): 1000,
        ('grams', 'kilograms'): 0.001,
        ('kilograms', 'grams'): 1000,
        ('inches', 'centimeters'): 2.54,
        ('centimeters', 'inches'): 1 / 2.54,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
             
class TemperatureConvertor:
    """
    A class to convert between different temperature scales.
    """

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9/5 + 32
    
class TimeConvertor:
    """
    A class to convert between different units of time.
    """

    conversion_factors = {
        ('seconds', 'minutes'): 1 / 60,
        ('minutes', 'seconds'): 60,
        ('minutes', 'hours'): 1 / 60,
        ('hours', 'minutes'): 60,
        ('hours', 'days'): 1 / 24,
        ('days', 'hours'): 24,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one time unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
                
class DataStorageConvertor:
    """
    A class to convert between different data storage units.
    """

    conversion_factors = {
        ('bytes', 'kilobytes'): 1 / 1024,
        ('kilobytes', 'bytes'): 1024,
        ('kilobytes', 'megabytes'): 1 / 1024,
        ('megabytes', 'kilobytes'): 1024,
        ('megabytes', 'gigabytes'): 1 / 1024,
        ('gigabytes', 'megabytes'): 1024,
        ('gigabytes', 'terabytes'): 1 / 1024,
        ('terabytes', 'gigabytes'): 1024,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one data storage unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class SpeedConvertor:
    """
    A class to convert between different speed units.
    """

    conversion_factors = {
        ('meters_per_second', 'kilometers_per_hour'): 3.6,
        ('kilometers_per_hour', 'meters_per_second'): 1 / 3.6,
        ('miles_per_hour', 'kilometers_per_hour'): 1.60934,
        ('kilometers_per_hour', 'miles_per_hour'): 1 / 1.60934,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one speed unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")

class PressureConvertor:
    """
    A class to convert between different pressure units.
    """

    conversion_factors = {
        ('pascals', 'bars'): 1 / 100000,
        ('bars', 'pascals'): 100000,
        ('pascals', 'atmospheres'): 1 / 101325,
        ('atmospheres', 'pascals'): 101325,
        ('bars', 'atmospheres'): 1 / 1.01325,
        ('atmospheres', 'bars'): 1.01325,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one pressure unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class EnergyConvertor:
    """
    A class to convert between different energy units.
    """

    conversion_factors = {
        ('joules', 'kilojoules'): 1 / 1000,
        ('kilojoules', 'joules'): 1000,
        ('calories', 'joules'): 4.184,
        ('joules', 'calories'): 1 / 4.184,
        ('kilowatt_hours', 'joules'): 3600000,
        ('joules', 'kilowatt_hours'): 1 / 3600000,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one energy unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class VolumeConvertor:
    """
    A class to convert between different volume units.
    """

    conversion_factors = {
        ('liters', 'milliliters'): 1000,
        ('milliliters', 'liters'): 1 / 1000,
        ('cubic_meters', 'liters'): 1000,
        ('liters', 'cubic_meters'): 1 / 1000,
        ('gallons', 'liters'): 3.78541,
        ('liters', 'gallons'): 1 / 3.78541,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one volume unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class AngleConvertor:
    """
    A class to convert between different angle units.
    """

    conversion_factors = {
        ('degrees', 'radians'): 3.141592653589793 / 180,
        ('radians', 'degrees'): 180 / 3.141592653589793,
        ('degrees', 'gradians'): 10 / 9,
        ('gradians', 'degrees'): 9 / 10,
        ('radians', 'gradians'): 200 / 3.141592653589793,
        ('gradians', 'radians'): 3.141592653589793 / 200,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one angle unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class FrequencyConvertor:
    """
    A class to convert between different frequency units.
    """

    conversion_factors = {
        ('hertz', 'kilohertz'): 1 / 1000,
        ('kilohertz', 'hertz'): 1000,
        ('megahertz', 'hertz'): 1000000,
        ('hertz', 'megahertz'): 1 / 1000000,
        ('gigahertz', 'hertz'): 1000000000,
        ('hertz', 'gigahertz'): 1 / 1000000000,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one frequency unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")

class CubicConvertor:
    """
    A class to convert between different cubic units.
    """

    conversion_factors = {
        ('cubic_meters', 'cubic_centimeters'): 1000000,
        ('cubic_centimeters', 'cubic_meters'): 1 / 1000000,
        ('cubic_inches', 'cubic_centimeters'): 16.3871,
        ('cubic_centimeters', 'cubic_inches'): 1 / 16.3871,
        ('cubic_feet', 'cubic_meters'): 0.0283168,
        ('cubic_meters', 'cubic_feet'): 1 / 0.0283168,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one cubic unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class LightConvertor:
    """
    A class to convert between different light units.
    """

    conversion_factors = {
        ('lumens', 'lux'): 1,
        ('lux', 'lumens'): 1,
        ('candela', 'lumens'): 12.57,
        ('lumens', 'candela'): 1 / 12.57,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one light unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")

class SoundConvertor:
    """
    A class to convert between different sound units.
    """

    conversion_factors = {
        ('decibels', 'pascals'): lambda db: 20 * (10 ** (db / 20)),
        ('pascals', 'decibels'): lambda pa: 20 * (pa / 20).log10(),
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one sound unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            func = cls.conversion_factors[key]
            return func(value)
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class DataRateConvertor:
    """
    A class to convert between different data rate units.
    """

    conversion_factors = {
        ('bps', 'Kbps'): 1 / 1000,
        ('Kbps', 'bps'): 1000,
        ('Kbps', 'Mbps'): 1 / 1000,
        ('Mbps', 'Kbps'): 1000,
        ('Mbps', 'Gbps'): 1 / 1000,
        ('Gbps', 'Mbps'): 1000,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one data rate unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class ForceConvertor:
    """
    A class to convert between different force units.
    """

    conversion_factors = {
        ('newtons', 'kilonewtons'): 1 / 1000,
        ('kilonewtons', 'newtons'): 1000,
        ('pounds_force', 'newtons'): 4.44822,
        ('newtons', 'pounds_force'): 1 / 4.44822,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one force unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class MagneticFieldConvertor:
    """
    A class to convert between different magnetic field units.
    """

    conversion_factors = {
        ('teslas', 'gauss'): 10000,
        ('gauss', 'teslas'): 1 / 10000,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one magnetic field unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class RadiationConvertor:
    """
    A class to convert between different radiation units.
    """

    conversion_factors = {
        ('sieverts', 'rems'): 100,
        ('rems', 'sieverts'): 1 / 100,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one radiation unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class DataDensityConvertor:
    """
    A class to convert between different data density units.
    """

    conversion_factors = {
        ('bits_per_square_inch', 'bits_per_square_centimeter'): 0.155,
        ('bits_per_square_centimeter', 'bits_per_square_inch'): 1 / 0.155,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one data density unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class AreaConvertor:
    """
    A class to convert between different Arena units.
    """
    conversion_factors = {
        ('square_meters', 'square_kilometers'): 1 / 1_000_000,
        ('square_kilometers', 'square_meters'): 1_000_000,
        ('square_meters', 'square_feet'): 10.7639,
        ('square_feet', 'square_meters'): 1 / 10.7639,
        ('acres', 'square_meters'): 4046.86,
        ('square_meters', 'acres'): 1 / 4046.86,
    }
    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one area unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class LengthConvertor:
    """
    A class to convert between different length units.
    """

    conversion_factors = {
        ('meters', 'kilometers'): 0.001,
        ('kilometers', 'meters'): 1000,
        ('meters', 'miles'): 0.000621371,
        ('miles', 'meters'): 1609.34,
        ('feet', 'meters'): 0.3048,
        ('meters', 'feet'): 3.28084,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one length unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class WeightConvertor:
    """
    A class to convert between different weight units.
    """

    conversion_factors = {
        ('grams', 'kilograms'): 0.001,
        ('kilograms', 'grams'): 1000,
        ('pounds', 'kilograms'): 0.453592,
        ('kilograms', 'pounds'): 2.20462,
        ('ounces', 'grams'): 28.3495,
        ('grams', 'ounces'): 1 / 28.3495,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one weight unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class WorkConvertor:
    """
    A class to convert between different work units.
    """

    conversion_factors = {
        ('joules', 'kilojoules'): 0.001,
        ('kilojoules', 'joules'): 1000,
        ('calories', 'joules'): 4.184,
        ('joules', 'calories'): 1 / 4.184,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one work unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class PowerConvertor:
    """
    A class to convert between different power units.
    """

    conversion_factors = {
        ('watts', 'kilowatts'): 0.001,
        ('kilowatts', 'watts'): 1000,
        ('horsepower', 'watts'): 745.7,
        ('watts', 'horsepower'): 1 / 745.7,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one power unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")

class MiscConvert:
    """Miscellaneous unit conversions"""
    conversion_factors = {
        ('celsius', 'fahrenheit'): lambda x: (x * 9/5) + 32,
        ('fahrenheit', 'celsius'): lambda x: (x - 32) * 5/9,
        ('joule', 'calorie'): 0.239006,
        ('calorie', 'joule'): 1 / 0.239006,
        ('atm', 'pa'): 101325,
        ('pa', 'atm'): 1 / 101325,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            if callable(factor):
                return factor(value)
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")

class GeometryConvert:
    """Geometry conversions: length, area, volume, angles"""
    conversion_factors = {
        ('meter', 'kilometer'): 0.001,
        ('kilometer', 'meter'): 1000,
        ('inch', 'cm'): 2.54,
        ('cm', 'inch'): 1/2.54,
        ('degree', 'radian'): 3.141592653589793/180,
        ('radian', 'degree'): 180/3.141592653589793,
        ('square_meter', 'square_foot'): 10.7639,
        ('square_foot', 'square_meter'): 1/10.7639,
        ('liter', 'milliliter'): 1000,
        ('milliliter', 'liter'): 1/1000,
        ('cubic_meter', 'liter'): 1000,
        ('liter', 'cubic_meter'): 1/1000,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            return value * cls.conversion_factors[key]
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")

class ResolutionConvert:
    """Screen resolution conversions"""
    conversion_factors = {
        ('dpi', 'dpcm'): 2.54,
        ('dpcm', 'dpi'): 1/2.54,
        ('pixels', 'inch'): lambda px, dpi=96: px/dpi,
        ('inch', 'pixels'): lambda inch, dpi=96: inch*dpi,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit, **kwargs):
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            if callable(factor):
                return factor(value, **kwargs)
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")

class HerzConvert:
    """Frequency conversions"""
    conversion_factors = {
        ('hz', 'khz'): 0.001,
        ('khz', 'hz'): 1000,
        ('hz', 'mhz'): 0.000001,
        ('mhz', 'hz'): 1_000_000,
        ('hz', 'ghz'): 0.000000001,
        ('ghz', 'hz'): 1_000_000_000,
        ('khz', 'mhz'): 0.001,
        ('mhz', 'khz'): 1000,
        ('khz', 'ghz'): 0.000001,
        ('ghz', 'khz'): 1_000_000,
        ('mhz', 'ghz'): 0.001,
        ('ghz', 'mhz'): 1000,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            return value * cls.conversion_factors[key]
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")

class LuminanceConvert:
    """Luminance conversions using conversion factors."""
    conversion_factors = {
        ('cd/m2', 'ftL'): 0.2919,
        ('ftL', 'cd/m2'): 1 / 0.2919,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            return value * cls.conversion_factors[key]
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")

class IlluminanceConvert:
    """Illuminance conversions using conversion factors."""
    conversion_factors = {
        ('lux', 'fc'): 0.092903,
        ('fc', 'lux'): 1 / 0.092903,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            return value * cls.conversion_factors[key]
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")

class AbsorbedDoseConvert:
    """Absorbed dose conversions using conversion factors."""
    conversion_factors = {
        ('Gy', 'rad'): 100,
        ('rad', 'Gy'): 1 / 100,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            return value * cls.conversion_factors[key]
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")

class DoseEquivalentConvert:
    """Dose equivalent conversions using conversion factors."""
    conversion_factors = {
        ('Sv', 'rem'): 100,
        ('rem', 'Sv'): 1 / 100,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            return value * cls.conversion_factors[key]
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")

class CatalyticActivityConvert:
    """Catalytic activity conversions using conversion factors."""
    conversion_factors = {
        ('katal', 'U'): 1_000_000,  # 1 katal = 1,000,000 enzyme units
        ('U', 'katal'): 1 / 1_000_000,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            return value * cls.conversion_factors[key]
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")

class RadioactivityConvert:
    """Radioactivity conversions using conversion factors."""
    conversion_factors = {
        ('becquerel', 'curie'): 2.7027e-11,
        ('curie', 'becquerel'): 3.7e10,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            return value * cls.conversion_factors[key]
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")
     
class WeightConvertor:
    """
    A class to convert between different weight units.
    """

    conversion_factors = {
        ('grams', 'kilograms'): 0.001,
        ('kilograms', 'grams'): 1000,
        ('pounds', 'kilograms'): 0.453592,
        ('kilograms', 'pounds'): 2.20462,
        ('ounces', 'grams'): 28.3495,
        ('grams', 'ounces'): 1 / 28.3495,
        ('tons', 'kilograms'): 907.185,
        ('kilograms', 'tons'): 1 / 907.185,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one weight unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class DensityConvertor:
    """
    A class to convert between different density units.
    """

    conversion_factors = {
        ('kg_per_cubic_meter', 'g_per_cubic_centimeter'): 0.001,
        ('g_per_cubic_centimeter', 'kg_per_cubic_meter'): 1000,
        ('pounds_per_cubic_foot', 'kg_per_cubic_meter'): 16.0185,
        ('kg_per_cubic_meter', 'pounds_per_cubic_foot'): 1 / 16.0185,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one density unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class WavelengthConvertor:
    """
    A class to convert between different wavelength units.
    """

    conversion_factors = {
        ('meters', 'nanometers'): 1e9,
        ('nanometers', 'meters'): 1e-9,
        ('meters', 'angstroms'): 1e10,
        ('angstroms', 'meters'): 1e-10,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one wavelength unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class ElectricChargeConvertor:
    """
    A class to convert between different electric charge units.
    """

    conversion_factors = {
        ('coulombs', 'ampere_hours'): 1 / 3600,
        ('ampere_hours', 'coulombs'): 3600,
        ('coulombs', 'statcoulombs'): 2997924580,
        ('statcoulombs', 'coulombs'): 1 / 2997924580,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one electric charge unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """        
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
class YieldConvertor:
    """
    A class to convert between different yield units.
    """

    conversion_factors = {
        ('tons_of_tnt', 'joules'): 4.184e9,
        ('joules', 'tons_of_tnt'): 1 / 4.184e9,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one yield unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        :raises ValueError: If the conversion is not supported.
        """        
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")

class MassConvertor:
    """
    A class to convert between different mass units.
    """

    conversion_factors = {
        ('grams', 'kilograms'): 0.001,
        ('kilograms', 'grams'): 1000,
        ('pounds', 'kilograms'): 0.453592,
        ('kilograms', 'pounds'): 2.20462,
        ('ounces', 'grams'): 28.3495,
        ('grams', 'ounces'): 1 / 28.3495,
        ('tons', 'kilograms'): 907.185,
        ('kilograms', 'tons'): 1 / 907.185,
        ('atomic_mass_units', 'grams'): 1.66053906660e-24,
        ('grams', 'atomic_mass_units'): 6.02214076e23,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one mass unit to another.

        :param value: The numerical value to convert.
        :param from_unit: The unit of the input value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        """
        key = (from_unit, to_unit)
        if key in cls.conversion_factors:
            factor = cls.conversion_factors[key]
            return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
