mod traits;
mod admin;
mod staff;

use traits::{Identity, AccessControl};
use admin::SuperAdmin;
use staff::Staff;

fn main() {
    let staff = Staff {
        username: String::from("Zkh"),
        departement: String::from("ITDEV"),
    };
    
    let admin = SuperAdmin {
        username: String::from("Admin"),
        admin_code: 12345,
    };
    
    println!("Staff: {} ({}) - Dept: {}", staff.get_name(), staff.get_role(), staff.get_departement());
    println!("Can read: {}, Can delete: {}", staff.can_read(), staff.can_delete());
    
    println!("Admin: {} ({}) - Code: {}", admin.get_name(), admin.get_role(), admin.get_admin_code());
    println!("Can read: {}, Can delete: {}", admin.can_read(), admin.can_delete());
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_rbac() {
        let staff = Staff {
            username: String::from("Zkh"),
            departement: String::from("ITDEV"),
        };
        
        assert_eq!(staff.get_name(), "Zkh");
        assert_eq!(staff.get_role(), "STAFF");
        assert!(staff.can_read());
        assert!(!staff.can_delete());
    }
}
