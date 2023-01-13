import React, { useState } from 'react';
import AuthSection from './AuthSection';
import PreviewSection from './PreviewSection';
export default function AuthPage(props) {
    return (
        <div>
            <PreviewSection></PreviewSection>
            <AuthSection setUser = {props.setUser}></AuthSection>
        </div>
    )
}