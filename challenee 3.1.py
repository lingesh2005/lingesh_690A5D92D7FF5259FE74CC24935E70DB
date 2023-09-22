def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices

# Get user input for product list
num_products = int(input("Enter the number of products: "))
products = [input(f"Enter product {i+1}: ") for i in range(num_products)]

# Get user input for target product
target_product = input("Enter the target product to search: ")

# Call linear_search_product function
result = linear_search_product(products, target_product)

# Display result
if result:
    print(f"The product '{target_product}' was found at indices: {result}")
else:
    print(f"The product '{target_product}' was not found.")
