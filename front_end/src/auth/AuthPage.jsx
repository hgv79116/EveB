import React, { useState } from 'react';
import AuthSection from './AuthSection';
import PreviewSection from './PreviewSection';
export default function AuthPage(props) {
    return (
        <div class = "row w-100 h-100">
            <div class="col"> 
                <PreviewSection></PreviewSection>
            </div>
            <div class="col d-flex justify-content-center align-items-center">
                <AuthSection setUser = {props.setUser}></AuthSection>
            </div>
        </div>
    )
}