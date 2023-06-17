import React, {useContext, useEffect, useState} from "react"
import CatalogItemImg from "../../media/catalog_item.png";
import Basket from "../../media/basket.png";
import {Link} from "react-router-dom";
import AuthContext from "../../context/AuthContext";
import {useParams} from "react-router";

function ProductList() {
    let {user, authTokens} = useContext(AuthContext)
    let [products, setProducts] = useState([])

    const params = useParams()
    let category_name = ""
    let request = ""

    switch(params.category) {
        case 'system_units':
            category_name = "Системные блоки"
            request = "system_unit_list"
            break

        case 'computer_kits':
            category_name = "Компьютеры в комплекте"
            request = "computer_kit_list"
            break

        case 'monitors':
            category_name = "Мониторы"
            request = "monitor_list"
            break

        case 'special_offers':
            category_name = "Спецпредложения"
            request = "special_offer_list"
            break
    }

    useEffect(() => {
        fetch(
            `http://127.0.0.1:8000/products/${request}/`, {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${authTokens.access}`,
                },
            }
        )
            .then(res => res.json())
            .then(data => setProducts(data));
    }, [])

    async function addBasketItem(id) {
        await fetch(
            'http://127.0.0.1:8000/basket_item', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${authTokens.access}`,
                },
                body: JSON.stringify({
                    'client': user.id,
                    'product': id
                })
            }
        )
        window.location.reload(false);
    }

    console.log(products)

    return (
        <div>
            <div className="grid grid-cols-3 grid-rows-1 px-1/10">
                <p className="h-fit w-fit text-xs font-light text-mainGray">
                    <Link to="/catalog" className="hover:underline">Каталог товаров</Link>
                    <span> > </span>
                    {((params.category === 'system_units')||(params.category === 'computer_kits'))
                        ?
                            <>
                                <Link to="/catalog/computers" className="hover:underline">Компьютеры</Link>
                                <span> > </span>
                                <Link to={`/catalog/computers/${params.category}`} className="hover:underline">{category_name}</Link>
                            </>
                        :
                            <Link to={`/catalog/${params.category}`} className="hover:underline">{category_name}</Link>
                    }
                </p>
                <h1 className="text-xl lg:text-3xl font-bold mb-10 text-center">{category_name}</h1>
                <p className="text-mainGray justify-self-end">{products.length} товара</p>
                <div/>
            </div>
            <div className="flex flex-wrap justify-center gap-5">
                {products.map((product) => (
                    <div className="w-72 bg-mainWhite py-5 px-10 drop-shadow-sm rounded-xl flex flex-col items-center">
                        <div className="w-64 h-64 shrink-0 grow-0 m-5">
                            <img src={product.picture ? "http://localhost:8000"+product.picture : CatalogItemImg} className="h-full w-full object-contain"/>
                        </div>
                        <Link to="catalog_item"><h2 className="hover:underline text-xl mb-5">{product.name}</h2></Link>
                        <p className="font-light mb-5 grow">{product.short_description}</p>
                        <div className="w-full flex justify-between items-center self-end">
                            <h2 className="text-2xl">{product.price} ₽</h2>
                            {product.basket_amount ?
                                <Link to="/basket" className="bg-grayWhite h-12 px-4 drop-shadow-sm rounded-xl flex items-center justify-center">
                                    <p className="whitespace-nowrap">В корзине</p>
                                </Link>
                                :
                                <button className="bg-mainOrange drop-shadow-sm rounded-xl h-12 w-12 flex justify-center items-center"
                                        onClick={() => addBasketItem(product.id)}
                                >
                                    <img src={Basket} className="h-8"/>
                                </button>
                                }
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default ProductList;