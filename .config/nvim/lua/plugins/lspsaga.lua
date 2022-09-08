local lspsaga = require 'lspsaga'
lspsaga.setup { -- defaults ...
  debug = false,
  use_saga_diagnostic_sign = true,
  -- diagnostic sign
  error_sign = "",
  warn_sign = "",
  hint_sign = "",
  infor_sign = "",
  diagnostic_header_icon = "   ",
  -- code action title icon
  code_action_icon = " ",
  code_action_prompt = {
    enable = true,
    sign = true,
    sign_priority = 40,
    virtual_text = {source = 'always'},
  },
  finder_definition_icon = "  ",
  finder_reference_icon = "  ",
  max_preview_lines = 10,
  finder_action_keys = {
    open = "o",
    vsplit = "s",
    split = "i",
    quit = "q",
    scroll_down = "<C-f>",
    scroll_up = "<C-b>",
  },
  code_action_keys = {
    quit = "q",
    exec = "<CR>",
  },
  rename_action_keys = {
    quit = "<C-c>",
    exec = "<CR>",
  },
  definition_preview_icon = "  ",
  border_style = "single",
  rename_prompt_prefix = "➤",
  server_filetype_map = {},
  diagnostic_prefix_format = "%d. ",
}

vim.cmd([[
" LspSagaFinder
nnoremap <silent> gh :Lspsaga lsp_finder<CR>

" Code action
nnoremap <silent>gx :Lspsaga code_action<CR>
vnoremap <silent>gx :<C-U>Lspsaga range_code_action<CR>
" Hover doc
nnoremap <silent>K :Lspsaga hover_doc<CR>
" REname
nnoremap <silent>gr :Lspsaga rename<CR>
" close rename win use <C-c> in insert mode or `q` in noremal mode or `:q`
" Preview Defintion
nnoremap <silent> gd :Lspsaga preview_definition<CR>
" Show & jump Diagnostic
nnoremap <silent> go :Lspsaga show_line_diagnostics<CR>
nnoremap <silent> gj :Lspsaga diagnostic_jump_next<CR>
nnoremap <silent> gk :Lspsaga diagnostic_jump_prev<CR>
"Float-term
nnoremap <silent> <A-d> :Lspsaga open_floaterm<CR>
tnoremap <silent> <A-d> <C-\><C-n>:Lspsaga close_floaterm<CR>


]])

