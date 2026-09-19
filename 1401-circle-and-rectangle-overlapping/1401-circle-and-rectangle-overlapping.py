class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """

        # Find closest point on rectangle to circle center
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        # Distance from circle center to closest point
        dx = xCenter - closestX
        dy = yCenter - closestY

        # Check whether it is inside/on the circle
        return dx * dx + dy * dy <= radius * radius