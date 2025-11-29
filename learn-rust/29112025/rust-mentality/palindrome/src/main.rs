// digunakan untuk mengakses command-line arguments
use std::env;

// Konstanta untuk konfigurasi
const MIN_LENGTH: usize = 1;

/* Utilisasi Enum
Mendefiniskan Varian: Found dan NotFound
Enum digunakan untuk merepresentasikan pilihan atau kondisi yang terbatas

Ekplisit, Type-safe, Readable, Rust idiom

Kapan harus menggunakan enum?
- kalau ada beberapa kemungkian hasil berbeda makna
- kalau mau compiler check semua case sudah di handle

Contoh Penggunaan enum

Sebelum:
struct IpAddressKind {
    ipv4_address: Option<String>,
    ipv6_address: Option<String>,
}

Sesudah:

enum IpAddressKind { V4, V6 }

struct IpAddress { kind: IpAddressKind, address: String }

let home = IpAddress {
    kind: IpAddressKind::V4,
    address: String::from("127.0.0.1"),
};

Ada juga enum yang membawa data terkait, seperti
yang digunakan pada project ini
*/

enum Result {
    Found(String),
    NotFound,
}

// Struct untuk menyimpan data palindrome
struct Palindrome;

impl Palindrome {
    fn is_palindrome(s: &str) -> bool {
        let chars: Vec<char> = s.chars().collect();
        chars.iter().eq(chars.iter().rev())
    }
    
    fn find_longest(input: &str) -> Result {
        let clean = input.to_lowercase().replace(|c: char| !c.is_alphanumeric(), "");
        let chars: Vec<char> = clean.chars().collect();
        let mut longest = String::new();
        
        for i in 0..chars.len() {
            for j in i+MIN_LENGTH..=chars.len() {
                let word: String = chars[i..j].iter().collect();
                if word.len() > longest.len() && Self::is_palindrome(&word) {
                    longest = word;
                }
            }
        }
        
        if longest.is_empty() {
            Result::NotFound
        } else {
            Result::Found(longest)
        }
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    
    if args.len() < 2 {
        println!("Cara pakai: cargo run -- \"text1\" \"text2\" ...");
        return;
    }
    
    let mut longest_overall = String::new();
    let mut from_input = String::new();
    
    // Cek setiap argumen
    for input in &args[1..] {
        match Palindrome::find_longest(input) {
            Result::Found(text) => {
                if text.len() > longest_overall.len() {
                    longest_overall = text;
                    from_input = input.clone();
                }
            }
            Result::NotFound => {}
        }
    }
    
    if longest_overall.is_empty() {
        println!("Tidak ada palindrome");
    } else {
        println!("Input: {}", from_input);
        println!("Palindrome terpanjang: {}", longest_overall);
        println!("Panjang: {}", longest_overall.len());
    }
}
