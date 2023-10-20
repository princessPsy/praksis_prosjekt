<?php

class App
{
    protected $controller = 'home';
    protected $method = 'index';
    protected $parameters = [];

    public funtion _construct()
    {

    }

    public function parseUrl()
    {
        if(isset($_GET['url']))
        {
            echo $_GET ['url'];
        }
    }
   
}