from .a_imports import *

 
class Interval:
    """
    Represents an interval on the real line.
    
    Supports different interval types:
    - open: (a, b) - excludes endpoints
    - closed: [a, b] - includes endpoints
    - half-open-left: [a, b) - includes left, excludes right
    - half-open-right: (a, b] - excludes left, includes right
    
    Examples:
        >>> i1 = Interval(0, 1, interval_type="closed")  # [0, 1]
        >>> i2 = Interval(0.5, 1.5, interval_type="open")  # (0.5, 1.5)
        >>> i3 = Interval(1, 2, interval_type="half-open-left")  # [1, 2)
    """
    
    VALID_TYPES = {"open", "closed", "half-open-left", "half-open-right"}
    
    def __init__(self, a: float, b: float, interval_type: str = "closed"):
        """
        Initialize an interval.
        
        Args:
            a: Left endpoint
            b: Right endpoint
            interval_type: Type of interval ("open", "closed", "half-open-left", "half-open-right")
        
        Raises:
            ValueError: If a >= b or invalid interval type
        """
        if a > b:
            raise ValueError(f"Left endpoint ({a}) must be <= right endpoint ({b})")
        
        if interval_type not in self.VALID_TYPES:
            raise ValueError(f"Invalid interval type. Must be one of {self.VALID_TYPES}")
        
        self.a = a
        self.b = b
        self.interval_type = interval_type
    
    # ===== STRING REPRESENTATIONS =====
    
    def __str__(self) -> str:
        """String representation of interval."""
        left_bracket = "[" if self._includes_left() else "("
        right_bracket = "]" if self._includes_right() else ")"
        return f"{left_bracket}{self.a}, {self.b}{right_bracket}"
    
    def __repr__(self) -> str:
        """Detailed representation."""
        return f"Interval({self.a}, {self.b}, interval_type='{self.interval_type}')"
    
    # ===== PRIVATE HELPER METHODS =====
    
    def _includes_left(self) -> bool:
        """Check if left endpoint is included."""
        return self.interval_type in {"closed", "half-open-left"}
    
    def _includes_right(self) -> bool:
        """Check if right endpoint is included."""
        return self.interval_type in {"closed", "half-open-right"}
    
    # ===== MEMBERSHIP TESTING =====
    
    def contains(self, x: float) -> bool:
        """
        Check if value x is in the interval.
        
        Args:
            x: Value to test
        
        Returns:
            True if x is in the interval
        
        Examples:
            >>> i = Interval(0, 1, "closed")
            >>> i.contains(0)
            True
            >>> i.contains(0.5)
            True
            >>> i.contains(1)
            True
            
            >>> i2 = Interval(0, 1, "open")
            >>> i2.contains(0)
            False
            >>> i2.contains(1)
            False
        """
        left_ok = (x > self.a) if not self._includes_left() else (x >= self.a)
        right_ok = (x < self.b) if not self._includes_right() else (x <= self.b)
        return left_ok and right_ok
    
    def __contains__(self, x: float) -> bool:
        """Support 'in' operator."""
        return self.contains(x)
    
    # ===== EQUALITY & COMPARISON =====
    
    def __eq__(self, other: 'Interval') -> bool:
        """Check if two intervals are equal."""
        if not isinstance(other, Interval):
            return False
        return (self.a == other.a and self.b == other.b and 
                self.interval_type == other.interval_type)
    
    def __ne__(self, other: 'Interval') -> bool:
        """Check if two intervals are not equal."""
        return not self.__eq__(other)
    
    def __lt__(self, other: 'Interval') -> bool:
        """Compare intervals by their left endpoint."""
        if not isinstance(other, Interval):
            return NotImplemented
        if self.a != other.a:
            return self.a < other.a
        return self.b < other.b
    
    def __le__(self, other: 'Interval') -> bool:
        """Less than or equal."""
        if not isinstance(other, Interval):
            return NotImplemented
        return self < other or self == other
    
    def __gt__(self, other: 'Interval') -> bool:
        """Greater than."""
        if not isinstance(other, Interval):
            return NotImplemented
        return other < self
    
    def __ge__(self, other: 'Interval') -> bool:
        """Greater than or equal."""
        if not isinstance(other, Interval):
            return NotImplemented
        return other <= self
    
    # ===== BASIC PROPERTIES =====
    
    def length(self) -> float:
        """
        Length (width) of the interval.
        
        Returns:
            b - a
        
        Examples:
            >>> Interval(0, 5).length()
            5
            >>> Interval(-2, 3).length()
            5
        """
        return self.b - self.a
    
    def midpoint(self) -> float:
        """
        Midpoint of the interval.
        
        Returns:
            (a + b) / 2
        
        Examples:
            >>> Interval(0, 10).midpoint()
            5.0
            >>> Interval(-1, 1).midpoint()
            0.0
        """
        return (self.a + self.b) / 2
    
    def is_empty(self) -> bool:
        """
        Check if interval is empty.
        
        For bounded intervals, this happens when a == b and at least one endpoint is excluded.
        
        Returns:
            True if interval contains no points
        """
        if self.a < self.b:
            return False
        if self.a > self.b:
            return True
        # a == b case
        return not (self._includes_left() and self._includes_right())
    
    def is_singleton(self) -> bool:
        """
        Check if interval contains exactly one point (a == b and both endpoints included).
        
        Returns:
            True if interval is a single point
        
        Examples:
            >>> Interval(5, 5, "closed").is_singleton()
            True
            >>> Interval(5, 5, "open").is_singleton()
            False
        """
        return (self.a == self.b and 
                self._includes_left() and self._includes_right())
    
    def is_bounded(self) -> bool:
        """
        Check if interval is bounded (finite endpoints).
        
        Returns:
            True for finite intervals
        """
        return (math.isfinite(self.a) and math.isfinite(self.b))
    
    # ===== SET OPERATIONS =====
    
    def intersection(self, other: 'Interval') -> Optional['Interval']:
        """
        Find intersection with another interval.
        
        Args:
            other: Another interval
        
        Returns:
            New interval representing intersection, or None if empty
        
        Examples:
            >>> i1 = Interval(0, 2, "closed")
            >>> i2 = Interval(1, 3, "closed")
            >>> result = i1.intersection(i2)
            >>> print(result)
            [1, 2]
            
            >>> i3 = Interval(0, 1, "closed")
            >>> i4 = Interval(2, 3, "closed")
            >>> i3.intersection(i4) is None
            True
        """
        if not isinstance(other, Interval):
            raise TypeError("Can only intersect with another Interval")
        
        # New endpoints
        new_a = max(self.a, other.a)
        new_b = min(self.b, other.b)
        
        # Empty intersection
        if new_a > new_b:
            return None
        
        # Determine new interval type at boundaries
        if new_a > self.a and new_a > other.a:
            left_type = "closed"
        elif new_a == self.a and new_a == other.a:
            # Both intervals have same left endpoint
            left_include = self._includes_left() and other._includes_left()
            left_type = "closed" if left_include else "open"
        elif new_a == self.a:
            left_type = "closed" if self._includes_left() else "open"
        else:  # new_a == other.a
            left_type = "closed" if other._includes_left() else "open"
        
        if new_b < self.b and new_b < other.b:
            right_type = "closed"
        elif new_b == self.b and new_b == other.b:
            # Both intervals have same right endpoint
            right_include = self._includes_right() and other._includes_right()
            right_type = "closed" if right_include else "open"
        elif new_b == self.b:
            right_type = "closed" if self._includes_right() else "open"
        else:  # new_b == other.b
            right_type = "closed" if other._includes_right() else "open"
        
        # Determine final type
        if left_type == "closed" and right_type == "closed":
            final_type = "closed"
        elif left_type == "open" and right_type == "open":
            final_type = "open"
        elif left_type == "closed" and right_type == "open":
            final_type = "half-open-right"
        else:
            final_type = "half-open-left"
        
        result = Interval(new_a, new_b, final_type)
        
        if result.is_empty():
            return None
        
        return result
    
    def union(self, other: 'Interval') -> Union['Interval', List['Interval']]:
        """
        Find union with another interval.
        
        Returns:
            Single interval if intervals overlap/touch, or list of two intervals if disjoint
        
        Examples:
            >>> i1 = Interval(0, 2, "closed")
            >>> i2 = Interval(1, 3, "closed")
            >>> result = i1.union(i2)
            >>> print(result)
            [0, 3]
            
            >>> i3 = Interval(0, 1, "closed")
            >>> i4 = Interval(2, 3, "closed")
            >>> i3.union(i4)
            [Interval(0, 1, ...), Interval(2, 3, ...)]
        """
        if not isinstance(other, Interval):
            raise TypeError("Can only union with another Interval")
        
        # Check if intervals overlap or touch
        if self.b < other.a or other.b < self.a:
            # Disjoint intervals
            return sorted([self, other])
        
        # Check if they touch at a single point
        if self.b == other.a:
            if not (self._includes_right() and other._includes_left()):
                # They don't actually touch
                return sorted([self, other])
        elif other.b == self.a:
            if not (other._includes_right() and self._includes_left()):
                # They don't actually touch
                return sorted([self, other])
        
        # Overlapping or touching intervals
        new_a = min(self.a, other.a)
        new_b = max(self.b, other.b)
        
        # Determine new type
        left_type = ("closed" if self.a < other.a and self._includes_left() or 
                    other.a < self.a and other._includes_left() else
                    ("closed" if self.a == other.a and 
                     self._includes_left() and other._includes_left() else "open"))
        
        right_type = ("closed" if self.b > other.b and self._includes_right() or 
                     other.b > self.b and other._includes_right() else
                     ("closed" if self.b == other.b and 
                      self._includes_right() and other._includes_right() else "open"))
        
        if left_type == "closed" and right_type == "closed":
            final_type = "closed"
        elif left_type == "open" and right_type == "open":
            final_type = "open"
        elif left_type == "closed":
            final_type = "half-open-right"
        else:
            final_type = "half-open-left"
        
        return Interval(new_a, new_b, final_type)
    
    def difference(self, other: 'Interval') -> Union['Interval', List['Interval'], None]:
        """
        Subtract another interval from this one.
        
        Returns:
            Single interval, list of intervals, or None if result is empty
        
        Examples:
            >>> i1 = Interval(0, 3, "closed")
            >>> i2 = Interval(1, 2, "closed")
            >>> result = i1.difference(i2)
            >>> len(result)
            2
        """
        if not isinstance(other, Interval):
            raise TypeError("Can only subtract another Interval")
        
        # No intersection means no change
        if self.b <= other.a or self.a >= other.b:
            return self
        
        # other completely contains self
        if other.a <= self.a and other.b >= self.b:
            return None
        
        # other is in the middle, creating two intervals
        if other.a > self.a and other.b < self.b:
            left_interval = Interval(self.a, other.a, 
                                    "closed" if self._includes_left() else "open")
            right_interval = Interval(other.b, self.b,
                                     "closed" if self._includes_right() else "open")
            return [left_interval, right_interval]
        
        # other overlaps left side
        if other.a <= self.a and other.b < self.b:
            return Interval(other.b, self.b, 
                          "closed" if self._includes_right() else "open")
        
        # other overlaps right side
        if other.a > self.a and other.b >= self.b:
            return Interval(self.a, other.a,
                          "closed" if self._includes_left() else "open")
        
        return self
    
    def complement(self) -> List['Interval']:
        """
        Find complement of interval (all real numbers NOT in the interval).
        
        Returns:
            List of intervals representing the complement
        
        Examples:
            >>> i = Interval(0, 1, "closed")
            >>> result = i.complement()
            >>> len(result)
            2
            >>> print(result[0])
            (-inf, 0)
            >>> print(result[1])
            (1, inf)
        """
        result = []
        
        # Left part: (-inf, a)
        if not self._includes_left():
            result.append(Interval(float('-inf'), self.a, "open"))
        else:
            result.append(Interval(float('-inf'), self.a, "half-open-right"))
        
        # Right part: (b, inf)
        if not self._includes_right():
            result.append(Interval(self.b, float('inf'), "open"))
        else:
            result.append(Interval(self.b, float('inf'), "half-open-left"))
        
        return result
    
    def is_subset_of(self, other: 'Interval') -> bool:
        """
        Check if this interval is a subset of another.
        
        Args:
            other: Another interval
        
        Returns:
            True if this ⊆ other
        """
        if not isinstance(other, Interval):
            raise TypeError("Can only compare with another Interval")
        
        # Check if our left endpoint is in other
        if self.a > other.a:
            left_ok = True
        elif self.a == other.a:
            left_ok = True if not self._includes_left() else other._includes_left()
        else:
            return False
        
        # Check if our right endpoint is in other
        if self.b < other.b:
            right_ok = True
        elif self.b == other.b:
            right_ok = True if not self._includes_right() else other._includes_right()
        else:
            return False
        
        return left_ok and right_ok
    
    # ===== ADVANCED PROPERTIES =====
    
    def split(self, x: float) -> Tuple['Interval', 'Interval']:
        """
        Split interval at point x into two intervals.
        
        Args:
            x: Point where to split (must be in interval)
        
        Returns:
            Tuple of two intervals (left, right)
        
        Raises:
            ValueError: If x not in interval
        """
        if not self.contains(x):
            raise ValueError(f"Point {x} not in interval {self}")
        
        left = Interval(self.a, x, 
                       "closed" if self._includes_left() else "open",
                       "half-open-right" if self._includes_left() else "open")
        right = Interval(x, self.b,
                        "half-open-left" if self._includes_right() else "open",
                        "closed" if self._includes_right() else "open")
        
        # Simplify types
        if left.a == left.b:
            left.interval_type = "closed"
        else:
            left.interval_type = "half-open-right" if self._includes_left() else "open"
        
        if right.a == right.b:
            right.interval_type = "closed"
        else:
            right.interval_type = "half-open-left" if self._includes_right() else "open"
        
        return left, right
    
    def scale(self, factor: float) -> 'Interval':
        """
        Scale interval by a factor.
        
        Args:
            factor: Scaling factor
        
        Returns:
            New scaled interval
        
        Examples:
            >>> i = Interval(1, 2)
            >>> i2 = i.scale(2)
            >>> print(i2)
            [2, 4]
        """
        if factor == 0:
            raise ValueError("Scale factor cannot be zero")
        
        if factor > 0:
            return Interval(self.a * factor, self.b * factor, self.interval_type)
        else:
            # Negative factor reverses interval
            return Interval(self.b * factor, self.a * factor, 
                          self._reverse_type(self.interval_type))
    
    def _reverse_type(self, itype: str) -> str:
        """Reverse interval type for negative scaling."""
        if itype == "half-open-left":
            return "half-open-right"
        elif itype == "half-open-right":
            return "half-open-left"
        else:
            return itype
    
    def translate(self, offset: float) -> 'Interval':
        """
        Translate interval by an offset.
        
        Args:
            offset: Amount to shift
        
        Returns:
            New translated interval
        
        Examples:
            >>> i = Interval(0, 1)
            >>> i2 = i.translate(5)
            >>> print(i2)
            [5, 6]
        """
        return Interval(self.a + offset, self.b + offset, self.interval_type)
    
    # ===== ARITHMETIC OPERATIONS =====
    
    def __add__(self, other: Union['Interval', float]) -> 'Interval':
        """Add interval or constant."""
        if isinstance(other, Interval):
            # Interval addition: all sums of elements
            return Interval(self.a + other.a, self.b + other.b, "closed")
        else:
            return self.translate(float(other))
    
    def __sub__(self, other: Union['Interval', float]) -> 'Interval':
        """Subtract interval or constant."""
        if isinstance(other, Interval):
            # Interval subtraction: all differences
            return Interval(self.a - other.b, self.b - other.a, "closed")
        else:
            return self.translate(-float(other))
    
    def __mul__(self, factor: Union[float, int]) -> 'Interval':
        """Multiply interval by scalar."""
        return self.scale(float(factor))
    
    def __rmul__(self, factor: Union[float, int]) -> 'Interval':
        """Right multiplication."""
        return self.scale(float(factor))
    
    def __truediv__(self, factor: Union[float, int]) -> 'Interval':
        """Divide interval by scalar."""
        if factor == 0:
            raise ValueError("Cannot divide by zero")
        return self.scale(1.0 / float(factor))
    
    # ===== STATIC METHODS FOR CREATION =====
    
    @staticmethod
    def open(a: float, b: float) -> 'Interval':
        """Create an open interval (a, b)."""
        return Interval(a, b, "open")
    
    @staticmethod
    def closed(a: float, b: float) -> 'Interval':
        """Create a closed interval [a, b]."""
        return Interval(a, b, "closed")
    
    @staticmethod
    def half_open_left(a: float, b: float) -> 'Interval':
        """Create a half-open interval [a, b)."""
        return Interval(a, b, "half-open-left")
    
    @staticmethod
    def half_open_right(a: float, b: float) -> 'Interval':
        """Create a half-open interval (a, b]."""
        return Interval(a, b, "half-open-right")
    
    @staticmethod
    def point(x: float) -> 'Interval':
        """Create a single-point interval {x}."""
        return Interval(x, x, "closed")
    
    @staticmethod
    def merge_intervals(intervals: List['Interval']) -> List['Interval']:
        """
        Merge a list of intervals, combining overlapping ones.
        
        Args:
            intervals: List of intervals to merge
        
        Returns:
            List of merged, non-overlapping intervals
        
        Examples:
            >>> i1 = Interval.closed(0, 2)
            >>> i2 = Interval.closed(1, 3)
            >>> i3 = Interval.closed(5, 6)
            >>> merged = Interval.merge_intervals([i1, i2, i3])
            >>> len(merged)
            2
        """
        if not intervals:
            return []
        
        if len(intervals) == 1:
            return intervals
        
        # Sort by left endpoint
        sorted_intervals = sorted(intervals)
        merged = [sorted_intervals[0]]
        
        for current in sorted_intervals[1:]:
            last = merged[-1]
            union_result = last.union(current)
            
            if isinstance(union_result, list):
                # Disjoint intervals
                merged.append(current)
            else:
                # Overlapping - replace last with union
                merged[-1] = union_result
        
        return merged
 
 
# ===== CONVENIENCE FUNCTIONS =====
 
def interval_from_endpoints(a: float, b: float, 
                           include_left: bool = True, 
                           include_right: bool = True) -> Interval:
    """
    Create interval from endpoints and inclusion flags.
    
    Args:
        a: Left endpoint
        b: Right endpoint
        include_left: Whether to include left endpoint
        include_right: Whether to include right endpoint
    
    Returns:
        New Interval
    """
    if include_left and include_right:
        itype = "closed"
    elif not include_left and not include_right:
        itype = "open"
    elif include_left:
        itype = "half-open-left"
    else:
        itype = "half-open-right"
    
    return Interval(a, b, itype)
 
 