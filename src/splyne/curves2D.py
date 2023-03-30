""" curves2D.py Contains definitions for 2D base curve functions E.G Bezier curves. """
import typing
from lerp import lerp, inv_lerp
import numpy as np
from enum import Enum

class Curve:
    def __init__(self,control_points: list[tuple[float,float]]) -> None:
        if len(control_points) < 2:
            raise Exception(f"Initializing curve failed. Not enough controls points given: {len(control_points)}. At least 2 control points are required")
        self.control_points = control_points
    
    def sample(self,t: float) -> tuple[float, float]:
        """
        Samples the curve position at t.
        --------------------------------
        t (float): The point on the curve as a 0 to 1 float.
        
        """

        index = lerp(0,len(self.control_points)-1,t)
        index_min = int(np.floor(index))
        index_max = int(np.ceil(index))

        p1 = self.control_points[index_min]
        p2 = self.control_points[index_max]
        t2 = index-index_min
        print(t2)

        return (lerp(p1[0],p2[0],t2),lerp(p1[1],p2[1],t2))
    
    def full_sample(self, resolution: int):
        """
        Samples the curve at a constant interval that is derived from the resolution argument given.
        --------------------------------
        resolution (int): The "resolution" or the amount of samples calculated.
        """

        samples = []
        for i in range(0,resolution):
            t = inv_lerp(0,resolution,i)
            s = self.sample(t)
            samples.append(s)
        return samples

class CurveLinear(Curve):
    pass

class CurveBezier(Curve):
    def sample(self, t: float) -> tuple[float, float]:
        """
        Samples the curve position at t.
        --------------------------------
        t (float): The point on the curve as a 0 to 1 float.
        """

        points = []
        for p in self.control_points:
            points.append(p)
        while len(points) != 1:
            new_points = []
            for i in range(len(points)-1):
                new_points.append((
                    lerp(points[i][0],points[i+1][0],t),
                    lerp(points[i][1],points[i+1][1],t)
                    ))
            points = new_points.copy()
        return points[0]




