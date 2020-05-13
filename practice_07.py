cumvec = 0
x = [8, 1, 3, 1, 3]
for (i in range(cumvec):
   if (i == 1) {
     cumvec[[i]] <- x[[i]]
   } else {
     cumvec[[i]] <- cumvec[[i - 1]] + x[[i]] 
   }

print(cumvec)