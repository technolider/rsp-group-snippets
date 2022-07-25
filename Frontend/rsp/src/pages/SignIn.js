import React, { useState } from 'react'
import logo from "../img/logo.png"
import { IdcardTwoTone, LockTwoTone } from '@ant-design/icons';
import { Button, Checkbox, Form, Input } from 'antd';
// import axios from 'axios';
// import validator from 'validator';

// const DOMEN_SERVER = '';
// const DOMEN_SITE = '';

export function SignIn() {
  const onFinish = (values) => {
    console.log('Received values of form: ', values);
  };
  return (
      <div className='mt-[159px] text-center overflow-hidden'>
        <img src={logo} alt="" className='w-[20%] h-[20%] inline' />
        <h1 className='font-medium text-[20px] mt-[29px] mb-[30px]'>Вход в кабинет</h1>
        <Form
          name="normal_login"
          className="login-form items-centerx"
          initialValues={{
          emember: true,
          }}
          onFinish={onFinish}
        >
          <div className="ml-[539px]">
          <Form.Item
            name="username"
            rules={[
              {
                required: true,
                message: 'Пожалуйста, введите свой логин',
              },
            ]}
            className='w-[40%]'
          >
            <Input prefix={<IdcardTwoTone />} placeholder="Логин" />
          </Form.Item>
          <Form.Item
            name="password"
            rules={[
              {
                required: true,
                message: 'Пожалуйста, введите свой пароль',
              },
            ]}
            className='w-[40%]'
          >
            <Input
              prefix={<LockTwoTone />}
              type="password"
              placeholder="Пароль"
            />
          </Form.Item>
          </div>
          <Form.Item>
            <Form.Item name="remember" valuePropName="checked" noStyle>
              <Checkbox>Запомнить меня</Checkbox>
            </Form.Item>
          </Form.Item>

          <Form.Item>
            <Button type="primary" htmlType="submit" className="login-form-button">
              Войти
            </Button>
          </Form.Item>
        </Form>
        <p className="font-normal text-[14px] text-[#8c8c8c] mt-[80px]">Если у вас есть проблемы со входом, обратитесь<br/>к администратору для восстановления доступа:<br/>
8 800 555-33-22 или super-admin@ummc.ru</p>
        <p className='font-normal text-[14px] text-[#8c8c8c] mt-[145px]'>© 2022, UMMC, v1.0</p>
        </div>
  )
}
