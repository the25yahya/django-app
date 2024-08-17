document.addEventListener('DOMContentLoaded', () => {
    // Select all elements with the class 'display-product'
    const displayProducts = document.querySelectorAll('.display-product');
    console.log(displayProducts);

    displayProducts.forEach(button => {
        // Find the parent product element
        const product = button.closest('.Product');

        // Get the product ID from the data attribute
        const productId = product.querySelector('.product-id').getAttribute('data-product-id');

        // Add an event listener to the button
        button.addEventListener('click', () => {
            // Construct the URL and redirect
            const url = `product?query=${productId}`;
            window.location.href = url; // Redirect to the URL
        });
    });
});
