import math


class Vec(tuple):
    """Vektor-Klasse für 2 bis n-dimensionale Koordinaten."""

    def __new__(cls, *args):
        return tuple.__new__(cls, args)

    def __add__(self, other):
        return Vec(*tuple(a + b for a, b in zip(self, other)))

    def __sub__(self, other):
        return Vec(*tuple(a - b for a, b in zip(self, other)))

    def __mul__(self, faktor):
        return Vec(*tuple(a * faktor for a in self))

    def __truediv__(self, divisor):
        return Vec(*tuple(a / divisor for a in self))

    def abstand(self, other):
        """Liefert den Manhatten-Abstand (https://de.wikipedia.org/wiki/Manhattan-Metrik) zwischen 2 Vektoren"""
        return sum(abs(a - b) for a, b in zip(self, other))

    def rotate2D(self, rotationspunkt, 𝜙):
        """
        Rotiert einen Punkt im Uhrzeigersinn um einen gegebenen Winkel um einen gegebenen Rotationspunkt (= Pivot)
        Der Winkel ist in Grad anzugeben
        """
        𝜙 = math.radians(𝜙)
        rx, ry = rotationspunkt
        px, py = self

        qx = rx + math.cos(𝜙) * (px - rx) - math.sin(𝜙) * (py - ry)
        qy = ry + math.sin(𝜙) * (px - rx) + math.cos(𝜙) * (py - ry)
        return Vec(qx, qy)


def pol2cart(radius, 𝜙) -> Vec:
    """Gibt zu einem Radius und einem Winkel die x,y-Koordinaten als Vektor zurück.
    Der Winkel ist in Grad anzugeben"""
    𝜙 = math.radians(𝜙)
    return Vec(math.cos(𝜙), math.sin(𝜙)) * radius
