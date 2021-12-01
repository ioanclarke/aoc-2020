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

    let nums = &password[..space];
    let lower = nums[..dash].parse::<usize>().unwrap() - 1;
    let upper = nums[dash+1..].parse::<usize>().unwrap() - 1;

    let letter = password.chars().nth(space + 1).unwrap();
    let pass = &password[colon+2..];

    let c1 = pass.chars().nth(lower).unwrap();
    let c2 = pass.chars().nth(upper).unwrap();

    (c1 == letter) ^ (c2 == letter)
}