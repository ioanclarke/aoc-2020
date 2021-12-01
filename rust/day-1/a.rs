use std::fs;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let inp = fs::read_to_string("input.txt")?;

    let nums: Vec<i32> = inp
        .lines()
        .map(|line| line.parse().unwrap())
        .collect();

    println!("{}", find_product(nums));
    Ok(())
}
    
    
fn find_product(nums: Vec<i32>) -> i32 {
    for s1 in &nums {
        for s2 in &nums {
            if s1 + s2 == 2020 {
                return s1 * s2;
            }
        }
    }
    0
}