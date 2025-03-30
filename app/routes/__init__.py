#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
define all routes here
"""

from fastapi import APIRouter

from . import users
from . import posts
from . import likes
from . import comments
from . import comment_likes

router = APIRouter()
router.include_router(users.router)
router.include_router(posts.router)
router.include_router(likes.router)
router.include_router(comments.router)
router.include_router(comment_likes.router)