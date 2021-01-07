call plug#begin('~/.config/nvim/plugged')
Plug 'lyokha/vim-xkbswitch'
Plug 'morhetz/gruvbox'
Plug 'ncm2/ncm2'
Plug 'ncm2/ncm2-jedi'
Plug 'ncm2/ncm2-bufword'
Plug 'roxma/nvim-yarp'
call plug#end()

let mapleader=" "
let g:XkbSwitchEnabled = 1

set number
set showcmd
set showmode
set undofile
set noswapfile
set lazyredraw
set nowrap
set smartcase ignorecase
set nowritebackup
set mouse=a
set showtabline=2
set laststatus=0
set shortmess+=c
set updatetime=300
set clipboard=unnamedplus
set completeopt=noinsert,menuone,noselect

" Colorscheme
	let g:gruvbox_contrast_dark='hard'
	colorscheme gruvbox
	hi Normal   ctermbg=black

" Perform dot commands over visual blocks:
	vnoremap . :normal .<CR>

" Save file as sudo on files that require root permission
	cnoremap w!! execute 'silent! write !sudo tee % >/dev/null' <bar> edit!

" Shortcutting split navigation, saving a keypress:
	map <C-h> <C-w>h
	map <C-j> <C-w>j
	map <C-k> <C-w>k
	map <C-l> <C-w>l

" Bindings
	map <leader>p :!opout <c-r>%<CR><CR>
	map <leader>c :w! \| !compiler "<c-r>%"<CR>
	map <leader>o :setlocal spell! spelllang=en_us<CR>
	inoremap <silent><expr><tab> pumvisible() ? "\<c-n>" : "\<tab>"
	inoremap <silent><expr><s-tab> pumvisible() ? "\<c-p>" : "\<s-tab>"
	set splitright

" Autocmd
	autocmd BufEnter * call ncm2#enable_for_buffer()
	autocmd BufWritePre * %s/\s\+$//e
	autocmd BufWritePre * %s/\n\+\%$//e

" Save file as sudo on files that require root permission
	cnoremap w!! execute 'silent! write !sudo tee % >/dev/null' <bar> edit!

" Automatically deletes all trailing whitespace and newlines at end of file on save.
	autocmd BufWritePre * %s/\s\+$//e
	autocmd BufWritePre * %s/\n\+\%$//e

" When shortcut files are updated, renew bash and ranger configs with new material:
	autocmd BufWritePost bm-files,bm-dirs !shortcuts

" Run xrdb whenever Xdefaults or Xresources are updated.
	autocmd BufRead,BufNewFile xresources,xdefaults set filetype=xdefaults
	autocmd BufWritePost Xresources,Xdefaults,xresources,xdefaults !xrdb %

" Recompile dwmblocks on config edit.
	autocmd BufWritePost ~/.local/src/dwmblocks/config.h !cd ~/.local/src/dwmblocks/; sudo make install && { killall -q dwmblocks;setsid -f dwmblocks }

" Turns off highlighting on the bits of code that are changed, so the line that is changed is highlighted but the actual text that has changed stands out on the line and is readable.
if &diff
    highlight! link DiffText MatchParen
endif
