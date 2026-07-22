from .topology_imports import*


class CofiniteTopology(Topology):
    """
    Cofinite topology where open sets are complements of finite sets (plus empty set).
    """

    def __init__(self, base_set):
        """
        Initialize cofinite topology.
        
        :param base_set: The underlying set
        """
        base_set = list(base_set)
        self.base_set = set(base_set)
        self.open_sets = [set()]  # Start with empty set
        
        # Add all complements of finite sets
        elements = list(self.base_set)
        for r in range(1, len(elements)):
            for combo in combinations(elements, r):
                complement = self.base_set - set(combo)
                self.open_sets.append(complement)
        
        self.open_sets.append(self.base_set)  # Add full set
        self.closed_sets = []
        self._compute_closed_sets()

