
class Analytic:
    """
    A comprehensive class for mathematical analysis including calculus, limits, series, and sequences.
    """
    
    # ==================== CONVERGENCE TESTS ====================
    
    @staticmethod
    def ratio_test(sequence, start_index=0):
        """
        Ratio test for convergence of series.
        
        :param sequence: List of terms in the series
        :param start_index: Starting index for calculation
        :return: Limit of ratio (if < 1, series converges)
        """
        ratios = []
        for i in range(start_index, len(sequence) - 1):
            if sequence[i] != 0:
                ratios.append(abs(sequence[i + 1] / sequence[i]))
        
        if ratios:
            return ratios[-1]  # Return the last ratio
        return 0
    
    @staticmethod
    def root_test(sequence, start_index=0):
        """
        Root test for convergence of series.
        
        :param sequence: List of terms in the series
        :param start_index: Starting index
        :return: Limit of nth root (if < 1, series converges)
        """
        roots = []
        for i in range(start_index, len(sequence)):
            roots.append(abs(sequence[i]) ** (1 / (i + 1)))
        
        if roots:
            return roots[-1]
        return 0
    
    @staticmethod
    def alternating_series_test(sequence):
        """
        Test for convergence of alternating series.
        Checks if terms decrease and approach zero.
        
        :param sequence: List of absolute values of terms
        :return: True if series likely converges
        """
        # Check if terms are decreasing
        decreasing = all(sequence[i] >= sequence[i + 1] for i in range(len(sequence) - 1))
        
        # Check if limit approaches zero
        limit_zero = sequence[-1] < 1e-10
        
        return decreasing and limit_zero
    
    # ==================== EXTREMA AND CRITICAL POINTS ====================
    
    
    # ==================== UTILITY FUNCTIONS ====================
    
    @staticmethod
    def verify_limit_behavior(func, x_val, num_points=100):
        """
        Verify limit behavior by sampling points approaching x_val.
        
        :param func: The function
        :param x_val: The limit point
        :param num_points: Number of sample points
        :return: List of function values at points approaching x_val
        """
        values = []
        for i in range(1, num_points + 1):
            delta = 1 / (i ** 2)
            try:
                values.append(func(x_val + delta))
            except:
                continue
        return values
    
