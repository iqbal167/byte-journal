/* 
Rust is compiled language, so we need to compile it first then run the binary file.

run with `rustc rust_array.rs && ./rust_array`
*/ 

fn main() {
    // Fixed-size array
    let arr = [1, 2, 3, 4, 5];
    println!("{:?}", arr);

    // Vector (dynamic array)
    let vec = vec![1, 2, 3, 4, 5];
    println!("{:?}", vec);
}
