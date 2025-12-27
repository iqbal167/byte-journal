# Trait Implementation - RBAC System

Simple role-based access control system demonstrating Rust trait implementation.

## Structure

- `traits.rs` - Defines `Identity` and `AccessControl` traits
- `admin.rs` - SuperAdmin with full permissions
- `staff.rs` - Staff with read-only permissions
- `main.rs` - Demo and tests

## Usage

```bash
# Run demo
cargo run

# Run tests
cargo test
```

## Output

```
Staff: Zkh (STAFF)
Can read: true, Can delete: false
Admin: Admin (SUPER_ADMIN)
Can read: true, Can delete: true
```

## Traits

```rust
pub trait Identity {
    fn get_name(&self) -> &str;
    fn get_role(&self) -> &str;
}

pub trait AccessControl {
    fn can_read(&self) -> bool;
    fn can_delete(&self) -> bool;
}
```
