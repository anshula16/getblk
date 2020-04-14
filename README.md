# GETBLK

```

The algorithms for reading and
writing disk blocks use the algorithm GETBLK (Figure 3 . 4) to allocate buffers from
the pool.
This section describes five typical scenarios the kernel may follow in getblk to
allocate a buffer for a disk block.
1. The kernel finds the block on its hash queue, and its buffer is free.
2. The kernel cannot find the block on the hash queue, so it allocates a buffer
from the free list.
3 . The kernel cannot find the block on the hash queue and, in attempting to
allocate a buffer from the free list (as in scenario 2) , finds a buffer on the
free list that has been marked .. delayed write." The kernel must write the
.. delayed write" buffer to disk and allocate another buffer.
4. The kernel cannot find the block on the hash queue, and the · free list of
buffers is empty.
5 . The kernel finds the block on the hash queue, but its buffer is currently busy.
```
