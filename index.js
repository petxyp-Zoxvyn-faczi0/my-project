// Төлеу батырмасының оқиға қосу
document.querySelector('#checkout').addEventListener('click', () => {
    if (cart.length === 0) {
        alert('Корзинаңыз бос, тауарларды таңдаңыз!');
    } else {
        let totalPrice = 0;
        cart.forEach(item => {
            totalPrice += item.price; // Жалпы бағаны есептеу
        });

        // Пайдаланушыдан төлем мәліметтерін сұрау (Бұл тек симуляция)
        let paymentConfirmed = confirm(`Сіздің тапсырысыңыз жасалды! Жалпы баға: ${totalPrice} ₸. Төлемді растаңыз.`);

        if (paymentConfirmed) {
            alert('Төлем қабылданды! Тапсырысыңыз өңделуде.');

            // Корзинаны тазалау
            cart = [];
            updateCartCount();
            updateCartDisplay();
        } else {
            alert('Төлем жасалмады. Сіз кейінірек қайта көре аласыз.');
        }
    }
});
document.querySelectorAll('.buy-button').forEach(button => {
    button.addEventListener('click', () => {
        const productCard = button.closest('.product-card');
        const productName = productCard.querySelector('h3').textContent;
        const productPrice = productCard.querySelector('p').textContent.split(":")[1].trim();
        const currentDate = new Date().toLocaleString();

        // Сатылған тауарды localStorage-ке қосу
        let history = JSON.parse(localStorage.getItem('history')) || [];
        history.push({ name: productName, price: productPrice, date: currentDate });
        localStorage.setItem('history', JSON.stringify(history));

        alert(`${productName} корзинаға қосылды`);
    });
});
// Сатып алу батырмасын басқанда корзинаға қосу
const buyButtons = document.querySelectorAll('.buy-button');
const cartItems = document.querySelector('#cart-items');
const totalPriceElem = document.querySelector('#total-price');
let totalPrice = 0;

buyButtons.forEach(button => {
    button.addEventListener('click', () => {
        const productName = button.closest('.product-card').querySelector('h3').textContent;
        const productPrice = parseFloat(button.closest('.product-card').querySelector('.discount-price').textContent.match(/\d+\.\d+/)[0]);
        
        // Корзинаға тауарды қосу
        const li = document.createElement('li');
        li.textContent = `${productName} - ${productPrice.toFixed(2)} ₸`;
        cartItems.appendChild(li);

        // Жалпы бағасын жаңарту
        totalPrice += productPrice;
        totalPriceElem.textContent = `Жалпы баға: ${totalPrice.toFixed(2)} ₸`;
    });
});

// Төлеу батырмасын басқанда хабарлама шығару
const checkoutButton = document.querySelector('#checkout');
const paymentMessage = document.querySelector('#payment-message');
checkoutButton.addEventListener('click', () => {
    // Жалпы баға есептелгенін тексеру
    if (totalPrice > 0) {
        paymentMessage.textContent = `Төлем жасалынды. Рақмет! Сіздің жалпы сомаңыз: ${totalPrice.toFixed(2)} ₸`;
        // Төлем сәтті аяқталған кезде жаңа бетке өту
        window.location.href = 'tolem.html';
    } else {
        paymentMessage.textContent = 'Корзина бос, тауар қосыңыз.';
    }
});
