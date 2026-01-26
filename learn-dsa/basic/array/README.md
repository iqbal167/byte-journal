# Array - Memory Allocation

## Array Memory Allocation Comparison

| Language | Type in Code | Memory Allocation | Resizable? |
|----------|--------------|-------------------|------------|
| Go | Array `[5]int` | Stack (Fixed) | No |
| Go | Slice `[]int` | Heap (Dynamic) | Yes (append) |
| Python | List | Heap (Dynamic) | Yes (append) |
| Rust | Array `[i32; 5]` | Stack (Fixed) | No |
| Rust | Vec `Vec<i32>` | Heap (Dynamic) | Yes (push) |
| TS | Array | Heap (Dynamic) | Yes (push) |

## Notes

- **Stack (Fixed)**: Fixed size, allocated on stack, faster
- **Heap (Dynamic)**: Dynamic size, allocated on heap, more flexible
- Go and Rust have separate types for dynamic arrays (Slice in Go, Vec in Rust)

## Stack vs Heap

### Stack
- **Location**: Part of RAM, managed by CPU
- **Size**: Limited (typically 1-8 MB)
- **Speed**: Very fast (LIFO - Last In First Out)
- **Allocation**: Automatic, happens at compile time
- **Lifetime**: Cleared when function returns
- **Use case**: Local variables, function parameters, fixed-size data

### Heap
- **Location**: Part of RAM, managed by program/OS
- **Size**: Large (limited by available RAM)
- **Speed**: Slower (requires memory management)
- **Allocation**: Manual/dynamic, happens at runtime
- **Lifetime**: Exists until explicitly freed or garbage collected
- **Use case**: Dynamic data, large objects, data that outlives function scope

### Memory Layout in RAM
```
┌─────────────────┐ High Address
│     Stack       │ ← Grows downward
│       ↓         │
├─────────────────┤
│   (Free Space)  │
├─────────────────┤
│       ↑         │
│      Heap       │ ← Grows upward
├─────────────────┤
│   Data Segment  │ (Global/Static variables)
├─────────────────┤
│   Code Segment  │ (Program instructions)
└─────────────────┘ Low Address
```

### Example
```rust
fn example() {
    let x = 5;              // Stack: fixed size, fast
    let arr = [1, 2, 3];    // Stack: fixed size array
    let vec = vec![1, 2];   // Heap: dynamic size vector
    //        ↑ Vec metadata on stack, data on heap
}
```
