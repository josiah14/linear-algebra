module LinearAlgebra.Vector
( makeVector
, multiplyScalar
, addVectors
, fromVector
, subtractVectors
) where
import Data.List

data Vector a = Vector [a] deriving (Show)

makeVector :: (Num a) => [a] -> Vector a
makeVector xs = Vector xs

fromVector :: Vector a -> [a]
fromVector (Vector v) = v

multiplyScalar :: (Num a) => a -> Vector a -> Vector a
multiplyScalar c (Vector v) = Vector $ map (c*) v

addVectors :: (Num a) => [Vector a] -> Vector a
addVectors vs = Vector $ map (foldl1 (+)) $ transpose $ map fromVector vs

subtractVectors :: (Num a) => [Vector a] -> Vector a
subtractVectors vs = Vector $ map (foldl1 (-)) $ transpose $ map fromVector vs

