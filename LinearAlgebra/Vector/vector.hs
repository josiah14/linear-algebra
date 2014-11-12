module LinearAlgebra.Vector
( makeVector
, multiplyScalar
, addVectors
, fromVector
, subtractVectors
, unitVector
) where
import Data.List

data Vector a = Vector [a] deriving (Show)

makeVector :: (Floating a) => [a] -> Vector a
makeVector = Vector

fromVector :: Vector a -> [a]
fromVector (Vector v) = v

multiplyScalar :: (Floating a) => a -> Vector a -> Vector a
multiplyScalar c (Vector v) = Vector $ map (c*) v

addVectors :: (Floating a) => [Vector a] -> Vector a
addVectors vs = Vector $ map sum $ transpose $ map fromVector vs

subtractVectors :: (Floating a) => [Vector a] -> Vector a
subtractVectors vs = Vector $ map (foldl1 (-)) $ transpose $ map fromVector vs

unitVector :: (Floating a) => Vector a -> Vector a
unitVector (Vector v) =
  let multiplier = sqrt ((/) 1 $ sum $ map (**2) v)
  in Vector $ map (multiplier*) v

