-- Create products table
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    category VARCHAR(50),
    stock INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample products
INSERT INTO products (name, description, price, category, stock) VALUES
('Laptop Pro X', 'High-performance laptop with 16GB RAM and 512GB SSD', 1299.99, 'Electronics', 10),
('Smartphone Y23', 'Latest smartphone with 128GB storage and 48MP camera', 799.99, 'Electronics', 15),
('Wireless Headphones', 'Noise-cancelling wireless headphones with 20h battery life', 149.99, 'Accessories', 25),
('Smart Watch', 'Fitness tracker with heart rate monitor and sleep tracking', 199.99, 'Wearables', 20),
('Bluetooth Speaker', 'Portable speaker with 360° sound and waterproof design', 79.99, 'Audio', 30); 