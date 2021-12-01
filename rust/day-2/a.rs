use std::fs;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let inp = fs::read_to_string("input.txt")?;

    let count = inp
        .lines()
        .filter(|line| !line.is_empty() && is_valid(line))
        .count();
    
    println!("{}", count);
    Ok(())

}

fn is_valid(password: &str) -> bool {
    let space = password.find(' ').unwrap();
    let dash = password.find('-').unwrap();
    let colon = password.find(':').unwrap();

    let nums = &password[0..space];
    let lower: usize = nums[0..dash].parse().unwrap();
    let upper: usize = nums[dash+1..].parse().unwrap();

    let letter = &password[space+1..space+2];
    let pass = &password[colon+2..];
    
    let count = pass.matches(letter).count();

    lower <= count && count <= upper
}