# -*- coding=utf-8 -*-

# Global scope
X = 3

def func(Y):
    # Local scope
    Z = X + Y
    return Z
    
func(1)

print func.__dict__
