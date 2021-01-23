import React from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import * as BsIcons from 'react-icons/bs';
import * as HiIcons from 'react-icons/hi';
import * as RiIcons from 'react-icons/ri';
import * as BiIcons from 'react-icons/bi';

export const SidebarData = [
  {
    title: 'Home',
    path: '/',
    icon:<AiIcons.AiFillHome />,
    cName: 'nav-text'
  },
  {
    title: 'Customer',
    path: '/customer',
    icon: <BsIcons.BsFillPeopleFill />,
    cName: 'nav-text'
  },
  {
    title: 'Employee',
    path: '/employee',
    icon: <HiIcons.HiDesktopComputer />,
    cName: 'nav-text'
  },
  {
    title: 'Category',
    path: '/category',
    icon: <RiIcons.RiBookReadFill />,
    cName: 'nav-text'
  },
  {
    title: 'Supplier',
    path: '/supplier',
    icon: <IoIcons.IoMdPeople />,
    cName: 'nav-text'
  },
  {
    title: 'Product',
    path: '/product',
    icon: <FaIcons.FaEnvelopeOpenText />,
    cName: 'nav-text'
  },
  {
    title: 'Order',
    path: '/order',
    icon: <FaIcons.FaCartPlus />,
    cName: 'nav-text'
  },
  {
    title: 'OrderDetail',
    path: '/orderdetail',
    icon: <BiIcons.BiMessageSquareDetail />,
    cName: 'nav-text'
  },
  {
    title: 'Shipper',
    path: '/shipper',
    icon: <IoIcons.IoMdHelpCircle />,
    cName: 'nav-text'
  }
];