#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : asio
Version  : 1.12.1
Release  : 6
URL      : https://sourceforge.net/projects/asio/files/asio/1.12.1%20%28Stable%29/asio-1.12.1.tar.gz
Source0  : https://sourceforge.net/projects/asio/files/asio/1.12.1%20%28Stable%29/asio-1.12.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSL-1.0
Requires: asio-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : openssl-dev

%description
asio version 1.12.1
Released Sunday, 15 April 2018.
See doc/index.html for API documentation and a tutorial.

%package dev
Summary: dev components for the asio package.
Group: Development
Provides: asio-devel = %{version}-%{release}

%description dev
dev components for the asio package.


%package license
Summary: license components for the asio package.
Group: Default

%description license
license components for the asio package.


%prep
%setup -q -n asio-1.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542383648
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1542383648
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/asio
cp LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/asio/LICENSE_1_0.txt
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.hpp
/usr/include/asio/associated_allocator.hpp
/usr/include/asio/associated_executor.hpp
/usr/include/asio/async_result.hpp
/usr/include/asio/basic_datagram_socket.hpp
/usr/include/asio/basic_deadline_timer.hpp
/usr/include/asio/basic_io_object.hpp
/usr/include/asio/basic_raw_socket.hpp
/usr/include/asio/basic_seq_packet_socket.hpp
/usr/include/asio/basic_serial_port.hpp
/usr/include/asio/basic_signal_set.hpp
/usr/include/asio/basic_socket.hpp
/usr/include/asio/basic_socket_acceptor.hpp
/usr/include/asio/basic_socket_iostream.hpp
/usr/include/asio/basic_socket_streambuf.hpp
/usr/include/asio/basic_stream_socket.hpp
/usr/include/asio/basic_streambuf.hpp
/usr/include/asio/basic_streambuf_fwd.hpp
/usr/include/asio/basic_waitable_timer.hpp
/usr/include/asio/bind_executor.hpp
/usr/include/asio/buffer.hpp
/usr/include/asio/buffered_read_stream.hpp
/usr/include/asio/buffered_read_stream_fwd.hpp
/usr/include/asio/buffered_stream.hpp
/usr/include/asio/buffered_stream_fwd.hpp
/usr/include/asio/buffered_write_stream.hpp
/usr/include/asio/buffered_write_stream_fwd.hpp
/usr/include/asio/buffers_iterator.hpp
/usr/include/asio/completion_condition.hpp
/usr/include/asio/connect.hpp
/usr/include/asio/coroutine.hpp
/usr/include/asio/datagram_socket_service.hpp
/usr/include/asio/deadline_timer.hpp
/usr/include/asio/deadline_timer_service.hpp
/usr/include/asio/defer.hpp
/usr/include/asio/detail/array.hpp
/usr/include/asio/detail/array_fwd.hpp
/usr/include/asio/detail/assert.hpp
/usr/include/asio/detail/atomic_count.hpp
/usr/include/asio/detail/base_from_completion_cond.hpp
/usr/include/asio/detail/bind_handler.hpp
/usr/include/asio/detail/buffer_resize_guard.hpp
/usr/include/asio/detail/buffer_sequence_adapter.hpp
/usr/include/asio/detail/buffered_stream_storage.hpp
/usr/include/asio/detail/call_stack.hpp
/usr/include/asio/detail/chrono.hpp
/usr/include/asio/detail/chrono_time_traits.hpp
/usr/include/asio/detail/completion_handler.hpp
/usr/include/asio/detail/concurrency_hint.hpp
/usr/include/asio/detail/conditionally_enabled_event.hpp
/usr/include/asio/detail/conditionally_enabled_mutex.hpp
/usr/include/asio/detail/config.hpp
/usr/include/asio/detail/consuming_buffers.hpp
/usr/include/asio/detail/cstddef.hpp
/usr/include/asio/detail/cstdint.hpp
/usr/include/asio/detail/date_time_fwd.hpp
/usr/include/asio/detail/deadline_timer_service.hpp
/usr/include/asio/detail/dependent_type.hpp
/usr/include/asio/detail/descriptor_ops.hpp
/usr/include/asio/detail/descriptor_read_op.hpp
/usr/include/asio/detail/descriptor_write_op.hpp
/usr/include/asio/detail/dev_poll_reactor.hpp
/usr/include/asio/detail/epoll_reactor.hpp
/usr/include/asio/detail/event.hpp
/usr/include/asio/detail/eventfd_select_interrupter.hpp
/usr/include/asio/detail/executor_op.hpp
/usr/include/asio/detail/fd_set_adapter.hpp
/usr/include/asio/detail/fenced_block.hpp
/usr/include/asio/detail/functional.hpp
/usr/include/asio/detail/gcc_arm_fenced_block.hpp
/usr/include/asio/detail/gcc_hppa_fenced_block.hpp
/usr/include/asio/detail/gcc_sync_fenced_block.hpp
/usr/include/asio/detail/gcc_x86_fenced_block.hpp
/usr/include/asio/detail/global.hpp
/usr/include/asio/detail/handler_alloc_helpers.hpp
/usr/include/asio/detail/handler_cont_helpers.hpp
/usr/include/asio/detail/handler_invoke_helpers.hpp
/usr/include/asio/detail/handler_tracking.hpp
/usr/include/asio/detail/handler_type_requirements.hpp
/usr/include/asio/detail/handler_work.hpp
/usr/include/asio/detail/hash_map.hpp
/usr/include/asio/detail/impl/buffer_sequence_adapter.ipp
/usr/include/asio/detail/impl/descriptor_ops.ipp
/usr/include/asio/detail/impl/dev_poll_reactor.hpp
/usr/include/asio/detail/impl/dev_poll_reactor.ipp
/usr/include/asio/detail/impl/epoll_reactor.hpp
/usr/include/asio/detail/impl/epoll_reactor.ipp
/usr/include/asio/detail/impl/eventfd_select_interrupter.ipp
/usr/include/asio/detail/impl/handler_tracking.ipp
/usr/include/asio/detail/impl/kqueue_reactor.hpp
/usr/include/asio/detail/impl/kqueue_reactor.ipp
/usr/include/asio/detail/impl/null_event.ipp
/usr/include/asio/detail/impl/pipe_select_interrupter.ipp
/usr/include/asio/detail/impl/posix_event.ipp
/usr/include/asio/detail/impl/posix_mutex.ipp
/usr/include/asio/detail/impl/posix_thread.ipp
/usr/include/asio/detail/impl/posix_tss_ptr.ipp
/usr/include/asio/detail/impl/reactive_descriptor_service.ipp
/usr/include/asio/detail/impl/reactive_serial_port_service.ipp
/usr/include/asio/detail/impl/reactive_socket_service_base.ipp
/usr/include/asio/detail/impl/resolver_service_base.ipp
/usr/include/asio/detail/impl/scheduler.ipp
/usr/include/asio/detail/impl/select_reactor.hpp
/usr/include/asio/detail/impl/select_reactor.ipp
/usr/include/asio/detail/impl/service_registry.hpp
/usr/include/asio/detail/impl/service_registry.ipp
/usr/include/asio/detail/impl/signal_set_service.ipp
/usr/include/asio/detail/impl/socket_ops.ipp
/usr/include/asio/detail/impl/socket_select_interrupter.ipp
/usr/include/asio/detail/impl/strand_executor_service.hpp
/usr/include/asio/detail/impl/strand_executor_service.ipp
/usr/include/asio/detail/impl/strand_service.hpp
/usr/include/asio/detail/impl/strand_service.ipp
/usr/include/asio/detail/impl/throw_error.ipp
/usr/include/asio/detail/impl/timer_queue_ptime.ipp
/usr/include/asio/detail/impl/timer_queue_set.ipp
/usr/include/asio/detail/impl/win_event.ipp
/usr/include/asio/detail/impl/win_iocp_handle_service.ipp
/usr/include/asio/detail/impl/win_iocp_io_context.hpp
/usr/include/asio/detail/impl/win_iocp_io_context.ipp
/usr/include/asio/detail/impl/win_iocp_serial_port_service.ipp
/usr/include/asio/detail/impl/win_iocp_socket_service_base.ipp
/usr/include/asio/detail/impl/win_mutex.ipp
/usr/include/asio/detail/impl/win_object_handle_service.ipp
/usr/include/asio/detail/impl/win_static_mutex.ipp
/usr/include/asio/detail/impl/win_thread.ipp
/usr/include/asio/detail/impl/win_tss_ptr.ipp
/usr/include/asio/detail/impl/winrt_ssocket_service_base.ipp
/usr/include/asio/detail/impl/winrt_timer_scheduler.hpp
/usr/include/asio/detail/impl/winrt_timer_scheduler.ipp
/usr/include/asio/detail/impl/winsock_init.ipp
/usr/include/asio/detail/io_control.hpp
/usr/include/asio/detail/is_buffer_sequence.hpp
/usr/include/asio/detail/is_executor.hpp
/usr/include/asio/detail/keyword_tss_ptr.hpp
/usr/include/asio/detail/kqueue_reactor.hpp
/usr/include/asio/detail/limits.hpp
/usr/include/asio/detail/local_free_on_block_exit.hpp
/usr/include/asio/detail/macos_fenced_block.hpp
/usr/include/asio/detail/memory.hpp
/usr/include/asio/detail/mutex.hpp
/usr/include/asio/detail/noncopyable.hpp
/usr/include/asio/detail/null_event.hpp
/usr/include/asio/detail/null_fenced_block.hpp
/usr/include/asio/detail/null_global.hpp
/usr/include/asio/detail/null_mutex.hpp
/usr/include/asio/detail/null_reactor.hpp
/usr/include/asio/detail/null_signal_blocker.hpp
/usr/include/asio/detail/null_socket_service.hpp
/usr/include/asio/detail/null_static_mutex.hpp
/usr/include/asio/detail/null_thread.hpp
/usr/include/asio/detail/null_tss_ptr.hpp
/usr/include/asio/detail/object_pool.hpp
/usr/include/asio/detail/old_win_sdk_compat.hpp
/usr/include/asio/detail/op_queue.hpp
/usr/include/asio/detail/operation.hpp
/usr/include/asio/detail/pipe_select_interrupter.hpp
/usr/include/asio/detail/pop_options.hpp
/usr/include/asio/detail/posix_event.hpp
/usr/include/asio/detail/posix_fd_set_adapter.hpp
/usr/include/asio/detail/posix_global.hpp
/usr/include/asio/detail/posix_mutex.hpp
/usr/include/asio/detail/posix_signal_blocker.hpp
/usr/include/asio/detail/posix_static_mutex.hpp
/usr/include/asio/detail/posix_thread.hpp
/usr/include/asio/detail/posix_tss_ptr.hpp
/usr/include/asio/detail/push_options.hpp
/usr/include/asio/detail/reactive_descriptor_service.hpp
/usr/include/asio/detail/reactive_null_buffers_op.hpp
/usr/include/asio/detail/reactive_serial_port_service.hpp
/usr/include/asio/detail/reactive_socket_accept_op.hpp
/usr/include/asio/detail/reactive_socket_connect_op.hpp
/usr/include/asio/detail/reactive_socket_recv_op.hpp
/usr/include/asio/detail/reactive_socket_recvfrom_op.hpp
/usr/include/asio/detail/reactive_socket_recvmsg_op.hpp
/usr/include/asio/detail/reactive_socket_send_op.hpp
/usr/include/asio/detail/reactive_socket_sendto_op.hpp
/usr/include/asio/detail/reactive_socket_service.hpp
/usr/include/asio/detail/reactive_socket_service_base.hpp
/usr/include/asio/detail/reactive_wait_op.hpp
/usr/include/asio/detail/reactor.hpp
/usr/include/asio/detail/reactor_fwd.hpp
/usr/include/asio/detail/reactor_op.hpp
/usr/include/asio/detail/reactor_op_queue.hpp
/usr/include/asio/detail/recycling_allocator.hpp
/usr/include/asio/detail/regex_fwd.hpp
/usr/include/asio/detail/resolve_endpoint_op.hpp
/usr/include/asio/detail/resolve_op.hpp
/usr/include/asio/detail/resolve_query_op.hpp
/usr/include/asio/detail/resolver_service.hpp
/usr/include/asio/detail/resolver_service_base.hpp
/usr/include/asio/detail/scheduler.hpp
/usr/include/asio/detail/scheduler_operation.hpp
/usr/include/asio/detail/scheduler_thread_info.hpp
/usr/include/asio/detail/scoped_lock.hpp
/usr/include/asio/detail/scoped_ptr.hpp
/usr/include/asio/detail/select_interrupter.hpp
/usr/include/asio/detail/select_reactor.hpp
/usr/include/asio/detail/service_registry.hpp
/usr/include/asio/detail/signal_blocker.hpp
/usr/include/asio/detail/signal_handler.hpp
/usr/include/asio/detail/signal_init.hpp
/usr/include/asio/detail/signal_op.hpp
/usr/include/asio/detail/signal_set_service.hpp
/usr/include/asio/detail/socket_holder.hpp
/usr/include/asio/detail/socket_ops.hpp
/usr/include/asio/detail/socket_option.hpp
/usr/include/asio/detail/socket_select_interrupter.hpp
/usr/include/asio/detail/socket_types.hpp
/usr/include/asio/detail/solaris_fenced_block.hpp
/usr/include/asio/detail/static_mutex.hpp
/usr/include/asio/detail/std_event.hpp
/usr/include/asio/detail/std_fenced_block.hpp
/usr/include/asio/detail/std_global.hpp
/usr/include/asio/detail/std_mutex.hpp
/usr/include/asio/detail/std_static_mutex.hpp
/usr/include/asio/detail/std_thread.hpp
/usr/include/asio/detail/strand_executor_service.hpp
/usr/include/asio/detail/strand_service.hpp
/usr/include/asio/detail/string_view.hpp
/usr/include/asio/detail/thread.hpp
/usr/include/asio/detail/thread_context.hpp
/usr/include/asio/detail/thread_group.hpp
/usr/include/asio/detail/thread_info_base.hpp
/usr/include/asio/detail/throw_error.hpp
/usr/include/asio/detail/throw_exception.hpp
/usr/include/asio/detail/timer_queue.hpp
/usr/include/asio/detail/timer_queue_base.hpp
/usr/include/asio/detail/timer_queue_ptime.hpp
/usr/include/asio/detail/timer_queue_set.hpp
/usr/include/asio/detail/timer_scheduler.hpp
/usr/include/asio/detail/timer_scheduler_fwd.hpp
/usr/include/asio/detail/tss_ptr.hpp
/usr/include/asio/detail/type_traits.hpp
/usr/include/asio/detail/variadic_templates.hpp
/usr/include/asio/detail/wait_handler.hpp
/usr/include/asio/detail/wait_op.hpp
/usr/include/asio/detail/win_event.hpp
/usr/include/asio/detail/win_fd_set_adapter.hpp
/usr/include/asio/detail/win_fenced_block.hpp
/usr/include/asio/detail/win_global.hpp
/usr/include/asio/detail/win_iocp_handle_read_op.hpp
/usr/include/asio/detail/win_iocp_handle_service.hpp
/usr/include/asio/detail/win_iocp_handle_write_op.hpp
/usr/include/asio/detail/win_iocp_io_context.hpp
/usr/include/asio/detail/win_iocp_null_buffers_op.hpp
/usr/include/asio/detail/win_iocp_operation.hpp
/usr/include/asio/detail/win_iocp_overlapped_op.hpp
/usr/include/asio/detail/win_iocp_overlapped_ptr.hpp
/usr/include/asio/detail/win_iocp_serial_port_service.hpp
/usr/include/asio/detail/win_iocp_socket_accept_op.hpp
/usr/include/asio/detail/win_iocp_socket_connect_op.hpp
/usr/include/asio/detail/win_iocp_socket_recv_op.hpp
/usr/include/asio/detail/win_iocp_socket_recvfrom_op.hpp
/usr/include/asio/detail/win_iocp_socket_recvmsg_op.hpp
/usr/include/asio/detail/win_iocp_socket_send_op.hpp
/usr/include/asio/detail/win_iocp_socket_service.hpp
/usr/include/asio/detail/win_iocp_socket_service_base.hpp
/usr/include/asio/detail/win_iocp_thread_info.hpp
/usr/include/asio/detail/win_iocp_wait_op.hpp
/usr/include/asio/detail/win_mutex.hpp
/usr/include/asio/detail/win_object_handle_service.hpp
/usr/include/asio/detail/win_static_mutex.hpp
/usr/include/asio/detail/win_thread.hpp
/usr/include/asio/detail/win_tss_ptr.hpp
/usr/include/asio/detail/winapp_thread.hpp
/usr/include/asio/detail/wince_thread.hpp
/usr/include/asio/detail/winrt_async_manager.hpp
/usr/include/asio/detail/winrt_async_op.hpp
/usr/include/asio/detail/winrt_resolve_op.hpp
/usr/include/asio/detail/winrt_resolver_service.hpp
/usr/include/asio/detail/winrt_socket_connect_op.hpp
/usr/include/asio/detail/winrt_socket_recv_op.hpp
/usr/include/asio/detail/winrt_socket_send_op.hpp
/usr/include/asio/detail/winrt_ssocket_service.hpp
/usr/include/asio/detail/winrt_ssocket_service_base.hpp
/usr/include/asio/detail/winrt_timer_scheduler.hpp
/usr/include/asio/detail/winrt_utils.hpp
/usr/include/asio/detail/winsock_init.hpp
/usr/include/asio/detail/work_dispatcher.hpp
/usr/include/asio/detail/wrapped_handler.hpp
/usr/include/asio/dispatch.hpp
/usr/include/asio/error.hpp
/usr/include/asio/error_code.hpp
/usr/include/asio/execution_context.hpp
/usr/include/asio/executor.hpp
/usr/include/asio/executor_work_guard.hpp
/usr/include/asio/experimental.hpp
/usr/include/asio/experimental/co_spawn.hpp
/usr/include/asio/experimental/detached.hpp
/usr/include/asio/experimental/impl/co_spawn.hpp
/usr/include/asio/experimental/impl/detached.hpp
/usr/include/asio/experimental/impl/redirect_error.hpp
/usr/include/asio/experimental/redirect_error.hpp
/usr/include/asio/generic/basic_endpoint.hpp
/usr/include/asio/generic/datagram_protocol.hpp
/usr/include/asio/generic/detail/endpoint.hpp
/usr/include/asio/generic/detail/impl/endpoint.ipp
/usr/include/asio/generic/raw_protocol.hpp
/usr/include/asio/generic/seq_packet_protocol.hpp
/usr/include/asio/generic/stream_protocol.hpp
/usr/include/asio/handler_alloc_hook.hpp
/usr/include/asio/handler_continuation_hook.hpp
/usr/include/asio/handler_invoke_hook.hpp
/usr/include/asio/handler_type.hpp
/usr/include/asio/high_resolution_timer.hpp
/usr/include/asio/impl/buffered_read_stream.hpp
/usr/include/asio/impl/buffered_write_stream.hpp
/usr/include/asio/impl/connect.hpp
/usr/include/asio/impl/defer.hpp
/usr/include/asio/impl/dispatch.hpp
/usr/include/asio/impl/error.ipp
/usr/include/asio/impl/error_code.ipp
/usr/include/asio/impl/execution_context.hpp
/usr/include/asio/impl/execution_context.ipp
/usr/include/asio/impl/executor.hpp
/usr/include/asio/impl/executor.ipp
/usr/include/asio/impl/handler_alloc_hook.ipp
/usr/include/asio/impl/io_context.hpp
/usr/include/asio/impl/io_context.ipp
/usr/include/asio/impl/post.hpp
/usr/include/asio/impl/read.hpp
/usr/include/asio/impl/read_at.hpp
/usr/include/asio/impl/read_until.hpp
/usr/include/asio/impl/serial_port_base.hpp
/usr/include/asio/impl/serial_port_base.ipp
/usr/include/asio/impl/spawn.hpp
/usr/include/asio/impl/src.cpp
/usr/include/asio/impl/src.hpp
/usr/include/asio/impl/system_context.hpp
/usr/include/asio/impl/system_context.ipp
/usr/include/asio/impl/system_executor.hpp
/usr/include/asio/impl/thread_pool.hpp
/usr/include/asio/impl/thread_pool.ipp
/usr/include/asio/impl/use_future.hpp
/usr/include/asio/impl/write.hpp
/usr/include/asio/impl/write_at.hpp
/usr/include/asio/io_context.hpp
/usr/include/asio/io_context_strand.hpp
/usr/include/asio/io_service.hpp
/usr/include/asio/io_service_strand.hpp
/usr/include/asio/ip/address.hpp
/usr/include/asio/ip/address_v4.hpp
/usr/include/asio/ip/address_v4_iterator.hpp
/usr/include/asio/ip/address_v4_range.hpp
/usr/include/asio/ip/address_v6.hpp
/usr/include/asio/ip/address_v6_iterator.hpp
/usr/include/asio/ip/address_v6_range.hpp
/usr/include/asio/ip/bad_address_cast.hpp
/usr/include/asio/ip/basic_endpoint.hpp
/usr/include/asio/ip/basic_resolver.hpp
/usr/include/asio/ip/basic_resolver_entry.hpp
/usr/include/asio/ip/basic_resolver_iterator.hpp
/usr/include/asio/ip/basic_resolver_query.hpp
/usr/include/asio/ip/basic_resolver_results.hpp
/usr/include/asio/ip/detail/endpoint.hpp
/usr/include/asio/ip/detail/impl/endpoint.ipp
/usr/include/asio/ip/detail/socket_option.hpp
/usr/include/asio/ip/host_name.hpp
/usr/include/asio/ip/icmp.hpp
/usr/include/asio/ip/impl/address.hpp
/usr/include/asio/ip/impl/address.ipp
/usr/include/asio/ip/impl/address_v4.hpp
/usr/include/asio/ip/impl/address_v4.ipp
/usr/include/asio/ip/impl/address_v6.hpp
/usr/include/asio/ip/impl/address_v6.ipp
/usr/include/asio/ip/impl/basic_endpoint.hpp
/usr/include/asio/ip/impl/host_name.ipp
/usr/include/asio/ip/impl/network_v4.hpp
/usr/include/asio/ip/impl/network_v4.ipp
/usr/include/asio/ip/impl/network_v6.hpp
/usr/include/asio/ip/impl/network_v6.ipp
/usr/include/asio/ip/multicast.hpp
/usr/include/asio/ip/network_v4.hpp
/usr/include/asio/ip/network_v6.hpp
/usr/include/asio/ip/resolver_base.hpp
/usr/include/asio/ip/resolver_query_base.hpp
/usr/include/asio/ip/resolver_service.hpp
/usr/include/asio/ip/tcp.hpp
/usr/include/asio/ip/udp.hpp
/usr/include/asio/ip/unicast.hpp
/usr/include/asio/ip/v6_only.hpp
/usr/include/asio/is_executor.hpp
/usr/include/asio/is_read_buffered.hpp
/usr/include/asio/is_write_buffered.hpp
/usr/include/asio/local/basic_endpoint.hpp
/usr/include/asio/local/connect_pair.hpp
/usr/include/asio/local/datagram_protocol.hpp
/usr/include/asio/local/detail/endpoint.hpp
/usr/include/asio/local/detail/impl/endpoint.ipp
/usr/include/asio/local/stream_protocol.hpp
/usr/include/asio/packaged_task.hpp
/usr/include/asio/placeholders.hpp
/usr/include/asio/posix/basic_descriptor.hpp
/usr/include/asio/posix/basic_stream_descriptor.hpp
/usr/include/asio/posix/descriptor.hpp
/usr/include/asio/posix/descriptor_base.hpp
/usr/include/asio/posix/stream_descriptor.hpp
/usr/include/asio/posix/stream_descriptor_service.hpp
/usr/include/asio/post.hpp
/usr/include/asio/raw_socket_service.hpp
/usr/include/asio/read.hpp
/usr/include/asio/read_at.hpp
/usr/include/asio/read_until.hpp
/usr/include/asio/seq_packet_socket_service.hpp
/usr/include/asio/serial_port.hpp
/usr/include/asio/serial_port_base.hpp
/usr/include/asio/serial_port_service.hpp
/usr/include/asio/signal_set.hpp
/usr/include/asio/signal_set_service.hpp
/usr/include/asio/socket_acceptor_service.hpp
/usr/include/asio/socket_base.hpp
/usr/include/asio/spawn.hpp
/usr/include/asio/ssl.hpp
/usr/include/asio/ssl/context.hpp
/usr/include/asio/ssl/context_base.hpp
/usr/include/asio/ssl/detail/buffered_handshake_op.hpp
/usr/include/asio/ssl/detail/engine.hpp
/usr/include/asio/ssl/detail/handshake_op.hpp
/usr/include/asio/ssl/detail/impl/engine.ipp
/usr/include/asio/ssl/detail/impl/openssl_init.ipp
/usr/include/asio/ssl/detail/io.hpp
/usr/include/asio/ssl/detail/openssl_init.hpp
/usr/include/asio/ssl/detail/openssl_types.hpp
/usr/include/asio/ssl/detail/password_callback.hpp
/usr/include/asio/ssl/detail/read_op.hpp
/usr/include/asio/ssl/detail/shutdown_op.hpp
/usr/include/asio/ssl/detail/stream_core.hpp
/usr/include/asio/ssl/detail/verify_callback.hpp
/usr/include/asio/ssl/detail/write_op.hpp
/usr/include/asio/ssl/error.hpp
/usr/include/asio/ssl/impl/context.hpp
/usr/include/asio/ssl/impl/context.ipp
/usr/include/asio/ssl/impl/error.ipp
/usr/include/asio/ssl/impl/rfc2818_verification.ipp
/usr/include/asio/ssl/impl/src.hpp
/usr/include/asio/ssl/rfc2818_verification.hpp
/usr/include/asio/ssl/stream.hpp
/usr/include/asio/ssl/stream_base.hpp
/usr/include/asio/ssl/verify_context.hpp
/usr/include/asio/ssl/verify_mode.hpp
/usr/include/asio/steady_timer.hpp
/usr/include/asio/strand.hpp
/usr/include/asio/stream_socket_service.hpp
/usr/include/asio/streambuf.hpp
/usr/include/asio/system_context.hpp
/usr/include/asio/system_error.hpp
/usr/include/asio/system_executor.hpp
/usr/include/asio/system_timer.hpp
/usr/include/asio/thread.hpp
/usr/include/asio/thread_pool.hpp
/usr/include/asio/time_traits.hpp
/usr/include/asio/ts/buffer.hpp
/usr/include/asio/ts/executor.hpp
/usr/include/asio/ts/internet.hpp
/usr/include/asio/ts/io_context.hpp
/usr/include/asio/ts/net.hpp
/usr/include/asio/ts/netfwd.hpp
/usr/include/asio/ts/socket.hpp
/usr/include/asio/ts/timer.hpp
/usr/include/asio/unyield.hpp
/usr/include/asio/use_future.hpp
/usr/include/asio/uses_executor.hpp
/usr/include/asio/version.hpp
/usr/include/asio/wait_traits.hpp
/usr/include/asio/waitable_timer_service.hpp
/usr/include/asio/windows/basic_handle.hpp
/usr/include/asio/windows/basic_object_handle.hpp
/usr/include/asio/windows/basic_random_access_handle.hpp
/usr/include/asio/windows/basic_stream_handle.hpp
/usr/include/asio/windows/object_handle.hpp
/usr/include/asio/windows/object_handle_service.hpp
/usr/include/asio/windows/overlapped_handle.hpp
/usr/include/asio/windows/overlapped_ptr.hpp
/usr/include/asio/windows/random_access_handle.hpp
/usr/include/asio/windows/random_access_handle_service.hpp
/usr/include/asio/windows/stream_handle.hpp
/usr/include/asio/windows/stream_handle_service.hpp
/usr/include/asio/write.hpp
/usr/include/asio/write_at.hpp
/usr/include/asio/yield.hpp

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/asio/LICENSE_1_0.txt
